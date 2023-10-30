window.BENCHMARK_DATA = {
  "lastUpdate": 1698690269078,
  "repoUrl": "https://github.com/Janelia-Trackathon-2023/traccuracy",
  "entries": {
    "Python Benchmark with pytest-benchmark": [
      {
        "commit": {
          "author": {
            "email": "msschwartz21@gmail.com",
            "name": "Morgan Schwartz",
            "username": "msschwartz21"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "9ef5c0a60bafa01ba2416fb2f6d435ad1d261a59",
          "message": "Merge pull request #62 from Janelia-Trackathon-2023/benchmark\n\nAdd basic set of performance benchmarking tests",
          "timestamp": "2023-10-11T11:56:33-07:00",
          "tree_id": "2311bcf0ded752234b676f6de32d13a15cd48cba",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/9ef5c0a60bafa01ba2416fb2f6d435ad1d261a59"
        },
        "date": 1697050935159,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.44346198594964636,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.254984715000006 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.548544191089205,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.8230071819999978 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.19312251187582147,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.178060239000018 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 0.006074829897877951,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 164.613662738 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 1.8927470976959035,
            "unit": "iter/sec",
            "range": "stddev: 0.03963486880011249",
            "extra": "mean: 528.3326025000008 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.05521454487306353,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.111169843000027 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 2.0658128062334917,
            "unit": "iter/sec",
            "range": "stddev: 0.023188769655713343",
            "extra": "mean: 484.0709656666604 msec\nrounds: 3"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "msschwartz21@gmail.com",
            "name": "msschwartz21",
            "username": "msschwartz21"
          },
          "committer": {
            "email": "msschwartz21@gmail.com",
            "name": "msschwartz21",
            "username": "msschwartz21"
          },
          "distinct": true,
          "id": "82fc051ffc64459be1726cee9a0521199055a804",
          "message": "Add badge for the benchmarking to readme",
          "timestamp": "2023-10-11T16:02:08-07:00",
          "tree_id": "e052c6461425521997feaf7b0880ac879a28d4bd",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/82fc051ffc64459be1726cee9a0521199055a804"
        },
        "date": 1697065732209,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.4682392034864301,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.135660560999952 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.589285282634235,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6969709400000283 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.14554139329580645,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 6.870897532000015 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 0.004767014111030251,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 209.77491920700004 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 1.783591940297145,
            "unit": "iter/sec",
            "range": "stddev: 0.06218887397209215",
            "extra": "mean: 560.6663595000327 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.05196118345686752,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 19.24513518499998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 1.8105263547824975,
            "unit": "iter/sec",
            "range": "stddev: 0.06094721567754861",
            "extra": "mean: 552.3255694999989 msec\nrounds: 2"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "msschwartz21@gmail.com",
            "name": "Morgan Schwartz",
            "username": "msschwartz21"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "ecbf250220c1677e9218a0300ac9e53c67c3e139",
          "message": "Improve the benchmarking workflow to generate a commit comment on PRs (#64)\n\n* Update benchmark ci workflow to generate a report\r\n\r\n* Improve report output\r\n\r\n* Add ID for cache step\r\n\r\n* Add missing dependency\r\n\r\n* Beautify benchmark commit table\r\n\r\n---------\r\n\r\nCo-authored-by: Benjamin Gallusser <bgallusser@googlemail.com>",
          "timestamp": "2023-10-12T20:24:11+02:00",
          "tree_id": "03860a2b20ca9afce54252fcb9db2fcc7a2a14f9",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/ecbf250220c1677e9218a0300ac9e53c67c3e139"
        },
        "date": 1697135376358,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.5908492832915347,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.692478992999952 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.7175831801935637,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3935666659999697 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.17585046249238723,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.68664981500001 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 0.006303631764377542,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 158.638708189 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 2.0421670512436205,
            "unit": "iter/sec",
            "range": "stddev: 0.058956596951455574",
            "extra": "mean: 489.6759055000075 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.06134712568614267,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.30068220499993 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 2.0703462990096737,
            "unit": "iter/sec",
            "range": "stddev: 0.05067068999095769",
            "extra": "mean: 483.0109825000477 msec\nrounds: 2"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "bgallusser@googlemail.com",
            "name": "Benjamin Gallusser",
            "username": "bentaculum"
          },
          "committer": {
            "email": "bgallusser@googlemail.com",
            "name": "Benjamin Gallusser",
            "username": "bentaculum"
          },
          "distinct": true,
          "id": "215336c1c5fda809da7cff17ed4e7ea2d4bb48b8",
          "message": "Update benchmark commit table",
          "timestamp": "2023-10-12T11:29:15-07:00",
          "tree_id": "76df5c64a0577dfc5a8fe0de0b48746ce3fcdff5",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/215336c1c5fda809da7cff17ed4e7ea2d4bb48b8"
        },
        "date": 1697135676508,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.6056600247226528,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6510913040000048 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.7170725270279407,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3945590750000036 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.1791020067206554,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.583410361000006 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 0.0063472629925833786,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 157.54822215000002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 2.1370823502234035,
            "unit": "iter/sec",
            "range": "stddev: 0.049816876937443015",
            "extra": "mean: 467.9276864999906 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.06149928547178184,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.260351519999972 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 2.0706832146586653,
            "unit": "iter/sec",
            "range": "stddev: 0.037520412671763356",
            "extra": "mean: 482.93239299997975 msec\nrounds: 3"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "msschwartz21@gmail.com",
            "name": "Morgan Schwartz",
            "username": "msschwartz21"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "73ddb1cad06d41beb25dde3c9b4cb076e3a3164a",
          "message": "Merge pull request #65 from Janelia-Trackathon-2023/log-benchmarks\n\nImprove benchmark action when running on repo forks",
          "timestamp": "2023-10-13T15:39:58-07:00",
          "tree_id": "5a0b8b83fbb209b0c1ece6220c4c17ebb686f95e",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/73ddb1cad06d41beb25dde3c9b4cb076e3a3164a"
        },
        "date": 1697237122099,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.6103223896559927,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6384783139999968 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.7240038315441172,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.38120816 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.19211030524957734,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.205342830000006 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 0.006042300404344065,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 165.49988135000004 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 2.4307685201370997,
            "unit": "iter/sec",
            "range": "stddev: 0.03190419610545715",
            "extra": "mean: 411.3925253333453 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.056208885193086144,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.79078159200003 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 2.3483704904920573,
            "unit": "iter/sec",
            "range": "stddev: 0.03876671809174468",
            "extra": "mean: 425.8271869999817 msec\nrounds: 3"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "msschwartz21@gmail.com",
            "name": "Morgan Schwartz",
            "username": "msschwartz21"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "b6b7d7ddb4500127a94eb54a9ef23c2985bbdfc8",
          "message": "Merge pull request #66 from Janelia-Trackathon-2023/benchmark-assertion-fix\n\nCorrect benchmarking tests assertion for wrong semantic edges",
          "timestamp": "2023-10-25T17:30:15-07:00",
          "tree_id": "e40f29880d49f94413b03469294cb8fa457ebcfc",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/b6b7d7ddb4500127a94eb54a9ef23c2985bbdfc8"
        },
        "date": 1698280624965,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.434106340662653,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.3035830310000165 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.5069699552641387,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.9725034779999646 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.15141368418119974,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 6.604422879000026 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 0.004643510494317815,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 215.354310327 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 1.8035937659084522,
            "unit": "iter/sec",
            "range": "stddev: 0.05663096132522826",
            "extra": "mean: 554.4485786666655 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.048052839490470525,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 20.810424744999978 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 1.747503178380709,
            "unit": "iter/sec",
            "range": "stddev: 0.006932425385260891",
            "extra": "mean: 572.2450249999724 msec\nrounds: 2"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "cmalinmayor@gmail.com",
            "name": "Caroline Malin-Mayor",
            "username": "cmalinmayor"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "082e010499343bda10ccd62625596a51e86a8e7c",
          "message": "Merge pull request #52 from Janelia-Trackathon-2023/dependabot/github_actions/actions/checkout-4\n\nci(dependabot): bump actions/checkout from 3 to 4",
          "timestamp": "2023-10-26T10:49:34-04:00",
          "tree_id": "aa2d9396cff6d9fb01ae9766286668048a9862fe",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/082e010499343bda10ccd62625596a51e86a8e7c"
        },
        "date": 1698332093729,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.5981115434270673,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6719289419999939 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.7369577004917652,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3569299829999864 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.18013652965859855,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.551344870999998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 0.006330954119484748,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 157.954074714 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 2.014511310629822,
            "unit": "iter/sec",
            "range": "stddev: 0.02196302051954228",
            "extra": "mean: 496.3983050000138 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.060786984540631854,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.450890063999964 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 2.15764129950012,
            "unit": "iter/sec",
            "range": "stddev: 0.035987610386586835",
            "extra": "mean: 463.46906700000545 msec\nrounds: 3"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "cmalinmayor@gmail.com",
            "name": "Caroline Malin-Mayor",
            "username": "cmalinmayor"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "674c0f8be3daac91f04403bd777d4a82de4ecef5",
          "message": "Merge pull request #63 from Janelia-Trackathon-2023/access_by_attr\n\nSpeed up accessing nodes/edges by attribute and node/edge attributes",
          "timestamp": "2023-10-27T15:38:30-04:00",
          "tree_id": "e7b827851c2a1f5a80f15a164156fd41660ea8a4",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/674c0f8be3daac91f04403bd777d4a82de4ecef5"
        },
        "date": 1698435836563,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.5675779168906919,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7618726349999747 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.7004545973451776,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4276442809999992 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.29925624173399434,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.3416178530000025 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 0.006002913919971993,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 166.585763736 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 1.9167146590720576,
            "unit": "iter/sec",
            "range": "stddev: 0.02186697105477821",
            "extra": "mean: 521.7260666666638 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.05414291829613084,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.469636131000016 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 1.9397951426383637,
            "unit": "iter/sec",
            "range": "stddev: 0.0016259474956348136",
            "extra": "mean: 515.5183544999886 msec\nrounds: 2"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "cmalinmayor@gmail.com",
            "name": "Caroline Malin-Mayor",
            "username": "cmalinmayor"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "ed2b7b111346cf8deef0e03bb7d68754cfd3fa84",
          "message": "Merge pull request #59 from bentaculum/faster_edge_errors\n\nSpeed up CTC edge errors",
          "timestamp": "2023-10-30T10:14:34-04:00",
          "tree_id": "8ea5f46158d6cfffd4e6a52ad69a56ee976f7be2",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/ed2b7b111346cf8deef0e03bb7d68754cfd3fa84"
        },
        "date": 1698675430056,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.6015459334672951,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6623834429999818 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.7482267779201673,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3364931990000173 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.3146030965320702,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.1786082559999898 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.394085526631285,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 717.3161049999806 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 2.4797900274495293,
            "unit": "iter/sec",
            "range": "stddev: 0.03000291276134732",
            "extra": "mean: 403.2599489999977 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.0562552099714961,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.776131322000026 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 2.4745657757559867,
            "unit": "iter/sec",
            "range": "stddev: 0.032005095595547255",
            "extra": "mean: 404.11130300001713 msec\nrounds: 3"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "cmalinmayor@gmail.com",
            "name": "Caroline Malin-Mayor",
            "username": "cmalinmayor"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "ed2b7b111346cf8deef0e03bb7d68754cfd3fa84",
          "message": "Merge pull request #59 from bentaculum/faster_edge_errors\n\nSpeed up CTC edge errors",
          "timestamp": "2023-10-30T10:14:34-04:00",
          "tree_id": "8ea5f46158d6cfffd4e6a52ad69a56ee976f7be2",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/ed2b7b111346cf8deef0e03bb7d68754cfd3fa84"
        },
        "date": 1698690262813,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.4388150216862543,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.27886455700002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.5370584895997171,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.8619945859999802 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.2849398661325083,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.509512423000018 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.1219872327299945,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 891.2757390000081 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 1.9930738868734224,
            "unit": "iter/sec",
            "range": "stddev: 0.07131322148458548",
            "extra": "mean: 501.73754549999217 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.047679493896834735,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 20.973376985999977 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 1.900133877162481,
            "unit": "iter/sec",
            "range": "stddev: 0.0630087197371194",
            "extra": "mean: 526.2787070000172 msec\nrounds: 2"
          }
        ]
      }
    ]
  }
}