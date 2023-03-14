import networkx as nx
import numpy as np
import pytest
import skimage as sk
from cell_tracking_metrics.matchers.iou import _match_nodes, match_iou_2d
from cell_tracking_metrics.tracking_data import TrackingData
from cell_tracking_metrics.tracking_graph import TrackingGraph


def get_annotated_image(img_size=256, num_labels=3, sequential=True, seed=1):
    np.random.seed(seed)
    num_labels_act = False
    trial = 0
    while num_labels != num_labels_act:
        if trial > 10:
            raise Exception(
                "Labels have merged despite 10 different random seeds."
                " Increase image size or reduce the number of labels"
            )
        im = np.zeros((img_size, img_size))
        points = img_size * np.random.random((2, num_labels))
        im[(points[0]).astype(int), (points[1]).astype(int)] = 1
        im = sk.filters.gaussian(im, sigma=5)
        blobs = im > 0.7 * im.mean()
        all_labels, num_labels_act = sk.measure.label(blobs, return_num=True)
        if num_labels != num_labels_act:
            seed += 1
            np.random.seed(seed)
            trial += 1

    if not sequential:
        labels_in_frame = np.unique(all_labels)
        for label in range(num_labels):
            curr_label = label + 1
            new_label = np.random.randint(1, num_labels * 100)
            while new_label in labels_in_frame:
                new_label = np.random.randint(1, num_labels * 100)
            labels_in_frame = np.append(labels_in_frame, new_label)
            label_loc = np.where(all_labels == curr_label)
            all_labels[:, :][label_loc] = new_label

    return all_labels.astype("int32")


def get_annotated_movie(
    img_size=256, labels_per_frame=3, frames=3, mov_type="sequential", seed=1
):
    if mov_type in ("sequential", "repeated"):
        sequential = True
    elif mov_type == "random":
        sequential = False
    else:
        raise ValueError(
            'mov_type must be one of "sequential", ' '"repeated" or "random"'
        )

    y = []
    while len(y) < frames:
        _y = get_annotated_image(
            img_size=img_size,
            num_labels=labels_per_frame,
            sequential=sequential,
            seed=seed,
        )
        y.append(_y)
        seed += 1

    y = np.stack(y, axis=0)  # expand to 3D

    if mov_type == "sequential":
        for frame in range(frames):
            if frame == 0:
                new_label = labels_per_frame
                continue
            for label in range(labels_per_frame):
                curr_label = label + 1
                new_label += 1
                label_loc = np.where(y[frame, :, :] == curr_label)
                y[frame, :, :][label_loc] = new_label

    return y.astype("int32")


def test__match_nodes():
    # Check shape error
    bad_shape = (2, 10, 10)
    with pytest.raises(ValueError):
        _match_nodes(np.zeros(bad_shape), np.zeros(bad_shape))

    # creat dummy image to test against
    num_labels = 5
    y1 = get_annotated_image(img_size=256, num_labels=num_labels, seed=1)
    # test same movie
    gtcells, rescells = _match_nodes(y1, y1)
    for gt_cell, res_cell in zip(gtcells, rescells):
        assert gt_cell == res_cell

    # test different movies (no assertions about matching)
    y2 = get_annotated_image(img_size=256, num_labels=num_labels, seed=10)
    gtcells, rescells = _match_nodes(y1, y2)


def test_match_iou_2d():
    # Bad input
    with pytest.raises(ValueError):
        match_iou_2d("not tracking data", "not tracking data")

    # shapes don't match
    with pytest.raises(ValueError):
        match_iou_2d(
            TrackingData(
                tracking_graph=nx.DiGraph(), segmentation=np.zeros((5, 10, 10))
            ),
            TrackingData(
                tracking_graph=nx.DiGraph(), segmentation=np.zeros((5, 10, 5))
            ),
        )

    n_labels = 3
    n_frames = 3
    movie = get_annotated_movie(
        labels_per_frame=n_labels, frames=n_frames, mov_type="repeated"
    )

    # We can assume each object is present and connected across each frame
    G = nx.DiGraph()
    for t in range(n_frames - 1):
        for i in range(1, n_labels + 1):
            G.add_edge(f"{i}_{t}", f"{i}_{t+1}")

    attrs = {}
    for t in range(n_frames):
        for i in range(1, n_labels + 1):
            attrs[f"{i}_{t}"] = {"t": t, "y": 0, "x": 0, "segmentation_id": i}
    nx.set_node_attributes(G, attrs)

    G = TrackingGraph(G)

    mapper = match_iou_2d(
        TrackingData(tracking_graph=G, segmentation=movie),
        TrackingData(tracking_graph=G, segmentation=movie),
    )

    # Check for correct number of pairs
    assert len(mapper) == n_frames * n_labels

    # gt and pred node should be the same
    for pair in mapper:
        assert pair[0] == pair[1]
