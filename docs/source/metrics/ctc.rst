CTC/AOGM Metrics
=================

These metrics are an implementation of the Cell Segmentation \& Tracking Challenge TRA and DET metrics,
as described on the Challenge `website <http://celltrackingchallenge.net/evaluation-methodology/>`_,
as well as the more general Acyclic Oriented Graph Measure (AOGM) metric, as described in `this
paper <https://journals.plos.org/plosone/article/file?id=10.1371/journal.pone.0144959&type=printable>`_.


DET
-----------------------

This metric assesses the solution's detection performance only, and therefore only measures
and annotates node errors.

Each type of node error is weighted based on how difficult it would be for a human to correct
the error by hand. The original Cell Tracking Challenge weights are used for all error types:

* Non-Split nodes are weighted 5
* False Negative nodes are weighted 10
* False Positive nodes are weighted 1

See Track Errors for the definition of each error type.

To compute the DET score for a dataset, the weighted sum of all node errors in the solution (:math:`AOGM-D`)
is normalized to a 0-1 value using a maximum potential error. The maximum potential error
(:math:`AOGM-D_{0}`) is defined as the cost of creating the ground truth nodes from scratch i.e. assume all
nodes in the ground truth are False Negative, and compute the weighed sum of errors
on this graph.

The final DET score is therefore:

.. math::

    DET = 1 - min(AOGM-D, AOGM-D_{0}) / AOGM-D_{0}


LNK
-----------------------

This metric assesses the solution's linking performance only, and therefore only measures
and annotates edge errors.

Each type of edge error is weighted based on how difficult it would be for a human to correct
the error by hand. The original Cell Tracking Challenge weights are used for all error types:

* Wrong-Semantic edges are weighted 1
* False Negative edges are weighted 1.5
* False Positive edges are weighted 1

See Track Errors for the definition of each error type.

To compute the LNK score for a dataset, the weighted sum of all edge errors in the solution (:math:`AOGM-A`)
is normalized to a 0-1 value using a maximum potential error. The maximum potential error
(:math:`AOGM-A_{0}`) is defined as the cost of creating the ground truth edges from scratch i.e. assume all
edges in the ground truth are False Negative, and compute the weighed sum of errors
on this graph.

The final LNK score is therefore:

.. math::

    LNK = 1 - min(AOGM-A, AOGM-A_{0}) / AOGM-A_{0}


TRA
-----------------------

The TRA measure assesses the solution's detection *and* tracking performance and therefore
includes both the node errors specified in DET (with identical weights) and the edge errors
computed by the general AOGM metric. Edge error weights are as follows:

* Wrong-Semantic edges are weighted 1
* False Negative edges are weighed 1.5
* False Positive edges are weighted 1

See Track Errors for the definition of each error type.

To compute the TRA score, the weighted sum of all node and edge errors in the solution (:math:`AOGM`)
is normalized to a 0-1 value using a maximum potential error. The maximum potential error (:math:`AOGM_{0}`) is again
defined based on the weighted error sum of an empty solution graph i.e. assume all nodes and edges in the ground truth
are False Negative, and computed the weighted sum of errors on this graph.

The final TRA score is therefore:

.. math::

    TRA = 1 - min(AOGM, AOGM_{0}) / AOGM_{0}


AOGM
-----------------------

The AOGM metric is a generalized graph measure that allows users to define their own
error weights for each type of node and edge error. The AOGM is simply the
weighted sum of all errors. This means that unlike the TRA and DET metrics,
the AOGM is **not** normalized to 0-1. The AOGM ranges between 0 (when
the predicted solution and ground truth are identical) and infinity (because in theory
an infinitely large predicted graph could be matched against ground truth), where
larger numbers mean more errors.

Note that the same process used to normalize TRA and DET can be used to normalize the
generalized AOGM - once the weights are chosen, compute the error sum of an empty solution
and use this to normalize the error sum of the predicted solution.