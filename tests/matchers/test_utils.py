import numpy as np
import skimage as sk


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
