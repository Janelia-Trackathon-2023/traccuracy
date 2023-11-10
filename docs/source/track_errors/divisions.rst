Division Errors
===============
Note: These are annotated on the parent nodes.

True Positive
-------------

A true positive division is a division event in which the parent and both daughters match between the ground truth and predicted graphs. True positive divisions are annotated on both the ground truth and predicted graphs.

The ``frame_buffer`` parameter allows for divisions to be classified as true positives if they occur within the specified number of frames of tolerance. This feature is useful in cases where the detection algorithm may split a cell into two detections before or after the split is annotated in the ground truth dataset.

For the given ground truth graph, the subsequent predicted graphs show examples of true positive divisions events with different ``frame_buffer`` specifications.

Ground truth::

                       2_3 -- 2_4
  1_0 -- 1_1 -- 1_2 -<
                       3_3 -- 3_4

Predicted -- true positive with ``frame_buffer=0``::

                       2_3 -- 2_4
  1_0 -- 1_1 -- 1_2 -<
                       3_3 -- 3_4

Predicted -- true positive with ``frame_buffer=1``::

                2_2 -- 2_3 -- 2_4
  1_0 -- 1_1 -<
                3_2 -- 3_3 -- 3_4

::

                              2_4
  1_0 -- 1_1 -- 1_2 -- 1_3 -<
                              3_4

False Negative
--------------

A false negative division applies to any case where the parent node is not linked to both correct daughters. False negative divisions are annotated on the ground truth graph.

Given the ground truth graph below, each of the subsequent prediction graphs would be classified as a false negative division.

Ground truth::

                2_2 -- 2_3
  1_0 -- 1_1 -<
                3_2 -- 3_3

                4_2 -- 4_3

Prediction -- only one daughter::

  1_0 -- 1_1 -- 2_2 -- 2_3

                3_2 -- 3_3

                4_2 -- 4_3

Prediction -- no daughters::

  1_0 -- 1_1

                2_2 -- 2_3

                3_2 -- 3_3

                4_2 -- 4_3

Prediction -- one incorrect daughter::

                  2_2 -- 2_3

                  3_2 -- 3_3
    1_0 -- 1_1 -<
                  4_2 -- 4_3

False Positive
--------------

A false positive division is any division event in the predicted graph that does not correspond to a division in the ground truth graph. False positive divisions are annotated on the predicted graph.

Ground truth::

  1_0 -- 1_1 -- 1_2 -- 1_3

                2_2 -- 2_3

Prediction::

                1_2 -- 1_3
  1_0 -- 1_1 -<
                2_2 -- 2_3

