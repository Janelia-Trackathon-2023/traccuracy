window.BENCHMARK_DATA = {
  "lastUpdate": 1737584410416,
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
          "id": "d3560d1a251d5fa2aa46ef99b07c2733f9151a9d",
          "message": "Merge pull request #69 from tlambert03/cov\n\ntest: enable codecov",
          "timestamp": "2023-11-01T15:23:06-04:00",
          "tree_id": "2547e4699635c504ed684367113a700d3f32bc0d",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/d3560d1a251d5fa2aa46ef99b07c2733f9151a9d"
        },
        "date": 1698866737370,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.5817122836141703,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7190628910000214 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.6992891928149043,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4300235299999713 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.2906603238910333,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.440442047999966 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.1352615489632343,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 880.8542849999981 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 2.091135562696463,
            "unit": "iter/sec",
            "range": "stddev: 0.05383950983483694",
            "extra": "mean: 478.2090735000111 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.06058757202938583,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.505035050999993 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 2.119178147832734,
            "unit": "iter/sec",
            "range": "stddev: 0.04463988939126471",
            "extra": "mean: 471.8810454999698 msec\nrounds: 2"
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
          "id": "32581bf8b6ecaf9ed61d7f94eb90622c8cc4cdd8",
          "message": "Merge pull request #70 from tlambert03/linting\n\nstyle: update pre-commit",
          "timestamp": "2023-11-01T22:13:49-04:00",
          "tree_id": "7313cc9fa794334c62749a0ae190e91bf92d4358",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/32581bf8b6ecaf9ed61d7f94eb90622c8cc4cdd8"
        },
        "date": 1698891329133,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7791582996298192,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2834362419999934 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8507003809005014,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1755020009999981 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4838820327192064,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.066619407999994 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8879091404004662,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 529.6865079999975 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.5110323632585883,
            "unit": "iter/sec",
            "range": "stddev: 0.018299419715445693",
            "extra": "mean: 284.8165144999974 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.13203105730490117,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 7.5739755509999895 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.5248450998009466,
            "unit": "iter/sec",
            "range": "stddev: 0.023647561247827863",
            "extra": "mean: 283.70040999999446 msec\nrounds: 4"
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
          "id": "5ff8bcf95e222d389e2eef56e4ebb480d171aba1",
          "message": "Merge pull request #71 from tlambert03/docs\n\ndocs: fix docs build, fix all build warnings, enable strict mode",
          "timestamp": "2023-11-01T22:27:08-04:00",
          "tree_id": "db5da5b332c59008dace80f55f3aedad2891e05f",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/5ff8bcf95e222d389e2eef56e4ebb480d171aba1"
        },
        "date": 1698892180051,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.5585960793565623,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7902023249999957 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.6987681177873055,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4310899059999542 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.29013097541614724,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.4467191880000314 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.1484041738850705,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 870.7735680000042 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 2.102879271972475,
            "unit": "iter/sec",
            "range": "stddev: 0.05924214151887511",
            "extra": "mean: 475.5384739999897 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.060844138287457335,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.43543697299998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 2.0885093978512943,
            "unit": "iter/sec",
            "range": "stddev: 0.04654495322910609",
            "extra": "mean: 478.810390333327 msec\nrounds: 3"
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
          "id": "27da5a762328bd383d3242469794351b3aa1fb17",
          "message": "Merge pull request #68 from Janelia-Trackathon-2023/dependabot/github_actions/actions/checkout-4\n\nci(dependabot): bump actions/checkout from 3 to 4",
          "timestamp": "2023-11-02T12:56:07-04:00",
          "tree_id": "ba5430c715d0265ac28f89b47c456c65efcf0d76",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/27da5a762328bd383d3242469794351b3aa1fb17"
        },
        "date": 1698944278502,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7662125096280074,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3051209519999816 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8511459577661792,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.174886622999992 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4692843205280406,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.1309043500000087 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8927468666252252,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 528.3326670000008 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.3528272324612853,
            "unit": "iter/sec",
            "range": "stddev: 0.029956549825187546",
            "extra": "mean: 298.25574975001246 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.12856614079115383,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 7.7780976690000045 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.392962514791874,
            "unit": "iter/sec",
            "range": "stddev: 0.023426230515521153",
            "extra": "mean: 294.727688750001 msec\nrounds: 4"
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
          "id": "000ea54038edb7ef8cf6e1e9f57cdfa18dff989c",
          "message": "Merge pull request #112 from yfukai/track_metrics_from_laptrack\n\nAdding track overlap metrics from `laptrack`",
          "timestamp": "2023-11-13T12:07:07-08:00",
          "tree_id": "eaf572ac14ba14f847fca1dddeb85ad47aac2cee",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/000ea54038edb7ef8cf6e1e9f57cdfa18dff989c"
        },
        "date": 1699906128075,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7793177577249725,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2831736349999971 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8524758119557483,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1730538109999884 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4734186933780463,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.1122951290000174 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8939036536817866,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 528.009964000006 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.5003158636906018,
            "unit": "iter/sec",
            "range": "stddev: 0.020919667195289537",
            "extra": "mean: 285.6885032500003 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11928006049911409,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.383630891999985 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.4913047392734344,
            "unit": "iter/sec",
            "range": "stddev: 0.02134483588180091",
            "extra": "mean: 286.42587075000137 msec\nrounds: 4"
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
          "id": "9d984f6d8a8a7ff42e190bc65777fad1693ea0cd",
          "message": "Merge pull request #103 from Janelia-Trackathon-2023/matcher\n\nRefactor existing `Matched` into separate `Matcher` which returns `Matched`",
          "timestamp": "2023-11-14T11:27:18-08:00",
          "tree_id": "2ef616eee3baecf131b1ace6aac9a677f90fbbcd",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/9d984f6d8a8a7ff42e190bc65777fad1693ea0cd"
        },
        "date": 1699990212550,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.6095398673813986,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6405817790000015 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.7229255289580252,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3832683449999763 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.30501353421152383,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.2785430409999776 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.1999238869079818,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 833.3861929999955 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 2.1391443263114494,
            "unit": "iter/sec",
            "range": "stddev: 0.047518338071840464",
            "extra": "mean: 467.4766390000021 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.05808276303513982,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.216811800000016 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 2.117246308435023,
            "unit": "iter/sec",
            "range": "stddev: 0.045581947098613754",
            "extra": "mean: 472.31160399998845 msec\nrounds: 3"
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
          "id": "d71f1b57f61ea86e79c1fe249b261176ce20ba0b",
          "message": "Merge pull request #109 from Janelia-Trackathon-2023/metrics-baseclass\n\nRefactor `Metrics` class to pass data into compute method not constructor",
          "timestamp": "2023-11-14T14:46:38-08:00",
          "tree_id": "c2e340b471a35309bde6b1591a9611719580f481",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/d71f1b57f61ea86e79c1fe249b261176ce20ba0b"
        },
        "date": 1700002103902,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7641618678326608,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3086232670000015 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8518045321856508,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1739782569999875 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.44880003099269605,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.22816383899999 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.941938286238188,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 514.9494230000187 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.535539706875081,
            "unit": "iter/sec",
            "range": "stddev: 0.023199262587836826",
            "extra": "mean: 282.84224839999297 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.10531088335706355,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.495694728999979 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.752543864730567,
            "unit": "iter/sec",
            "range": "stddev: 0.030176478875578228",
            "extra": "mean: 266.4858922500031 msec\nrounds: 4"
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
          "id": "f8f352cd7543a4ecf90651a2ae459f75ad274703",
          "message": "Merge pull request #121 from Janelia-Trackathon-2023/pr-template\n\nAdd pull request and issue templates",
          "timestamp": "2023-11-17T11:52:42-08:00",
          "tree_id": "5099adae4013cf6e1114ddec78d27644b62e663e",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/f8f352cd7543a4ecf90651a2ae459f75ad274703"
        },
        "date": 1700250883603,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7889598213910978,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2674916680000194 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8677371201362694,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1524227520000068 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4489741252377399,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.227299845999994 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8927513841567607,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 528.3314060000066 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.536717055168083,
            "unit": "iter/sec",
            "range": "stddev: 0.023018396483604348",
            "extra": "mean: 282.74809220000634 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11068658473101896,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.034518523000003 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.713368794674698,
            "unit": "iter/sec",
            "range": "stddev: 0.030159233453140488",
            "extra": "mean: 269.29724875000005 msec\nrounds: 4"
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
          "id": "c9e6197c004b4fa67c3963f18a95fff4d76bdffd",
          "message": "Merge pull request #122 from Janelia-Trackathon-2023/pr-templates-link\n\nCreate general pr template",
          "timestamp": "2023-11-17T12:01:23-08:00",
          "tree_id": "e086a6af0324d50cac575171cefce800f8d32df5",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/c9e6197c004b4fa67c3963f18a95fff4d76bdffd"
        },
        "date": 1700251387193,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.778143163719271,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2851105639999787 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.851031241447111,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1750449939999612 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.44718828743219996,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.2361945249999735 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.9148535330256273,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 522.2331539999914 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.569741967791678,
            "unit": "iter/sec",
            "range": "stddev: 0.023247077175447595",
            "extra": "mean: 280.132292199994 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.10504558788223974,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.51967636300003 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.7507894544434506,
            "unit": "iter/sec",
            "range": "stddev: 0.029320947359145432",
            "extra": "mean: 266.6105394999789 msec\nrounds: 4"
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
          "id": "e5df26a63ddcd2da4ce9c9c43cfc0d0b34b77647",
          "message": "Merge pull request #123 from Janelia-Trackathon-2023/remove-headers\n\nRemove Pr template headers",
          "timestamp": "2023-11-17T12:03:07-08:00",
          "tree_id": "bd966f0ca43e26e894ed126e0bf9830bce3ed1c3",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/e5df26a63ddcd2da4ce9c9c43cfc0d0b34b77647"
        },
        "date": 1700251500981,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7720005551981073,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.29533585599998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8866273374088791,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1278695770000127 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4696847294140318,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.129087741999996 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 2.0303015810983114,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 492.5376650000146 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.6883980403201897,
            "unit": "iter/sec",
            "range": "stddev: 0.022275348582860795",
            "extra": "mean: 271.12041299999987 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11477190794659538,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.712933485999997 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.9509680401622487,
            "unit": "iter/sec",
            "range": "stddev: 0.026600280616226067",
            "extra": "mean: 253.1025282499968 msec\nrounds: 4"
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
          "id": "d4ee393b1dbddd3955d99e686719fa464c0a4d55",
          "message": "Merge pull request #124 from Janelia-Trackathon-2023/docs-fixes\n\nFix subclass docstrings for sphinx autoapi",
          "timestamp": "2023-11-20T11:52:33-08:00",
          "tree_id": "742ee63151fd7347343dba8b920012f2eaff1e51",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/d4ee393b1dbddd3955d99e686719fa464c0a4d55"
        },
        "date": 1700510062131,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7864971433421004,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2714604349999945 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8687202155039128,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1511186019999968 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4457788672373546,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.2432647070000087 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8740503144615528,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 533.6036030000173 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.5064516455630224,
            "unit": "iter/sec",
            "range": "stddev: 0.04095443679380986",
            "extra": "mean: 285.18858979999777 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.10491661207423435,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.531379066 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.6788592309583636,
            "unit": "iter/sec",
            "range": "stddev: 0.027845127822246935",
            "extra": "mean: 271.82339339999544 msec\nrounds: 5"
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
          "id": "64431d80b5943b6992ddeaef7142e07b5c2ca310",
          "message": "Merge pull request #118 from Janelia-Trackathon-2023/run_metrics\n\nUpdate `run_metrics` to take instantiated `Matchers` and `Metrics` as input",
          "timestamp": "2023-11-20T13:11:27-08:00",
          "tree_id": "1a084334358cf5e5c7725763f53d178ea7f2843d",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/64431d80b5943b6992ddeaef7142e07b5c2ca310"
        },
        "date": 1700514803255,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.757697458711974,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.319787981999994 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.815119163464662,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2268144889999917 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.43818240213157206,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.2821546349999977 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.751141011524784,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 571.0562390000007 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.603668511192661,
            "unit": "iter/sec",
            "range": "stddev: 0.029821894083601544",
            "extra": "mean: 277.495001799997 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11006743863334285,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.085339065 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.6140914939486,
            "unit": "iter/sec",
            "range": "stddev: 0.02782634119324373",
            "extra": "mean: 276.6947105999918 msec\nrounds: 5"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "66853113+pre-commit-ci[bot]@users.noreply.github.com",
            "name": "pre-commit-ci[bot]",
            "username": "pre-commit-ci[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "2ed94df23575a8a93cc82e82adb0c2fd9315d691",
          "message": "ci(pre-commit.ci): autoupdate (#113)\n\nupdates:\r\n- [github.com/crate-ci/typos: v1.16.21 → v1.16.23](https://github.com/crate-ci/typos/compare/v1.16.21...v1.16.23)\r\n- [github.com/astral-sh/ruff-pre-commit: v0.1.3 → v0.1.4](https://github.com/astral-sh/ruff-pre-commit/compare/v0.1.3...v0.1.4)\r\n\r\nCo-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>\r\nCo-authored-by: Draga Doncila Pop <17995243+DragaDoncila@users.noreply.github.com>",
          "timestamp": "2023-11-28T14:00:59+11:00",
          "tree_id": "86ea1c5292bd6f9a8b035093d43588e0636bc4f9",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/2ed94df23575a8a93cc82e82adb0c2fd9315d691"
        },
        "date": 1701140559706,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.76483486846922,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.307471770999996 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8437890924322348,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1851302759999953 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4457106910855777,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.2436078380000026 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8614257643506527,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 537.2226060000003 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.622413629270416,
            "unit": "iter/sec",
            "range": "stddev: 0.03202086546226646",
            "extra": "mean: 276.05903200000057 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11082435035857705,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.02328772300001 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.6660173064875976,
            "unit": "iter/sec",
            "range": "stddev: 0.029746176415754364",
            "extra": "mean: 272.77558079999835 msec\nrounds: 5"
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
          "id": "ef50a446c5ee52d2581dc23a73c2e46325537d49",
          "message": "Merge pull request #104 from tlambert03/future\n\nstyle: cleanup string type annotations",
          "timestamp": "2023-11-29T14:09:25-05:00",
          "tree_id": "3807271d1f76ffb31f426ddcb1d2f2574828b20a",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/ef50a446c5ee52d2581dc23a73c2e46325537d49"
        },
        "date": 1701285078036,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7678622249258596,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.302316961999992 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8568395922338184,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.167079589999986 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4477917452565962,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.2331809610000164 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8744695485485496,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 533.4842600000229 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.7009250464374412,
            "unit": "iter/sec",
            "range": "stddev: 0.028335503834475313",
            "extra": "mean: 270.2027161999979 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11095609632149325,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.012573739999993 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.6448240443477786,
            "unit": "iter/sec",
            "range": "stddev: 0.02223632011231523",
            "extra": "mean: 274.36166680000724 msec\nrounds: 5"
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
          "id": "a61d295fc9428d49ece133597b93d1dafb62aa03",
          "message": "Merge pull request #128 from Janelia-Trackathon-2023/pre-commit-ci-update-config\n\nci(pre-commit.ci): autoupdate",
          "timestamp": "2023-12-06T17:21:40-05:00",
          "tree_id": "2736ac22433a4b770333b2861952905317ffeadd",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/a61d295fc9428d49ece133597b93d1dafb62aa03"
        },
        "date": 1701901414559,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7266606301078821,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3761582209999972 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8528358164816634,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1725586339999836 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4439543472581501,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.252483855999998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.863514265927508,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 536.6205230000105 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.67555665026375,
            "unit": "iter/sec",
            "range": "stddev: 0.030155535026090422",
            "extra": "mean: 272.0676335999997 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.1054126519428929,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.486527295999991 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.6677385979931247,
            "unit": "iter/sec",
            "range": "stddev: 0.029693741218863617",
            "extra": "mean: 272.6475656000048 msec\nrounds: 5"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "ad3f68d2f89ac718475111b5cb08776057760f12",
          "message": "Add CTC format checks in loader (#119)\n\n* Add CTC format checks in loader\r\n\r\n- unique positive integer track IDs\r\n- indicated parent IDs present\r\n- parent tracklet ends before child tracklet starts (gaps possible)\r\n- masks contain all detections as indicated in tracks file, and vice versa.\r\n\r\n* Add complete object name for docs cross referencing\r\n\r\n* Update docstrings and error messages\r\n\r\n* Add soft connected component check for CTC data\r\n\r\n* Remove ctc checks in benchmarking\r\n\r\n* Expose helper functions in ctc loader\r\n\r\n* Add separate benchmark for ctc loader checks\r\n\r\n---------\r\n\r\nCo-authored-by: msschwartz21 <msschwartz21@gmail.com>",
          "timestamp": "2023-12-10T12:34:25+01:00",
          "tree_id": "72b3ca9e243cbe8233ee06a77fbab8b68b657308",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/ad3f68d2f89ac718475111b5cb08776057760f12"
        },
        "date": 1702208170897,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.762385353948531,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3116726270000072 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8637356685825222,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1577616120000016 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.4750245438283627,
            "unit": "iter/sec",
            "range": "stddev: 0.0037961304042288015",
            "extra": "mean: 404.036397333338 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4426554114811742,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.2590935839999986 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8813036641988345,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 531.5462989999844 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.5590558873373035,
            "unit": "iter/sec",
            "range": "stddev: 0.023191451229756913",
            "extra": "mean: 280.9733905999849 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11205782058934108,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.923964385000005 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.760784196765182,
            "unit": "iter/sec",
            "range": "stddev: 0.03187056641937951",
            "extra": "mean: 265.90198949999433 msec\nrounds: 4"
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
          "id": "15a7d5f264304d69983693457c7c070858b443da",
          "message": "Merge pull request #126 from Janelia-Trackathon-2023/results-class\n\nCreate a `Results` class for storing metric output with associated metadata",
          "timestamp": "2023-12-15T10:46:35-08:00",
          "tree_id": "6e3cd964e98b8a7122000d8f4d470797b19d0194",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/15a7d5f264304d69983693457c7c070858b443da"
        },
        "date": 1702666145203,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7848303359038168,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2741607380000062 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.860803200419466,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1617057180000074 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.453893352018302,
            "unit": "iter/sec",
            "range": "stddev: 0.002004714905130895",
            "extra": "mean: 407.5156726666667 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4481806347804113,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.2312432139999885 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8580259344003647,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 538.2056199999852 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.583434292115107,
            "unit": "iter/sec",
            "range": "stddev: 0.030309166295722716",
            "extra": "mean: 279.0619050000089 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.10580026618777752,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.451772061000014 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.6090396991667895,
            "unit": "iter/sec",
            "range": "stddev: 0.029572792408642728",
            "extra": "mean: 277.0820171999958 msec\nrounds: 5"
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
          "id": "c681c3d0c80ef2e195b7d2cffac41efb294be15d",
          "message": "Merge pull request #133 from Janelia-Trackathon-2023/pre-commit-ci-update-config\n\nci(pre-commit.ci): autoupdate",
          "timestamp": "2024-01-08T11:19:49-05:00",
          "tree_id": "383a6649f77103071747f4da24790bdc25a7d2b0",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/c681c3d0c80ef2e195b7d2cffac41efb294be15d"
        },
        "date": 1704730899740,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8063553282244571,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2401480649999996 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8612042629831475,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1611647120000015 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.4619537140950274,
            "unit": "iter/sec",
            "range": "stddev: 0.0012848548824511558",
            "extra": "mean: 406.1814786666626 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.44860199804189727,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.2291474499999993 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8651781177489695,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 536.1418250000014 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.588260934310525,
            "unit": "iter/sec",
            "range": "stddev: 0.02932647314645283",
            "extra": "mean: 278.6865332000019 msec\nrounds: 5"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.10557592509476711,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.471856383000002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.5946320057563215,
            "unit": "iter/sec",
            "range": "stddev: 0.03057010024195997",
            "extra": "mean: 278.19259340000144 msec\nrounds: 5"
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
          "id": "6f6406ecb68e9e0fc05b788552820f8f3e6ff24f",
          "message": "Merge pull request #131 from Janelia-Trackathon-2023/dependabot/github_actions/actions/setup-python-5\n\nci(dependabot): bump actions/setup-python from 4 to 5",
          "timestamp": "2024-01-08T14:04:47-05:00",
          "tree_id": "b15ae83b3cb7cc9a6917f28d6bc8287278b74637",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/6f6406ecb68e9e0fc05b788552820f8f3e6ff24f"
        },
        "date": 1704740804035,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8065308955406792,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2398781070000098 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8530998989937372,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1721956610000035 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.361047482083848,
            "unit": "iter/sec",
            "range": "stddev: 0.009639210456699037",
            "extra": "mean: 423.5408256666678 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.43024340959372925,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.3242657010000016 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.773417777363707,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 563.8829229999942 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.296416297478581,
            "unit": "iter/sec",
            "range": "stddev: 0.027905010753436585",
            "extra": "mean: 303.359742749997 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.10350242817902301,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.661609081000009 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.5632940642142743,
            "unit": "iter/sec",
            "range": "stddev: 0.033057813854844444",
            "extra": "mean: 280.6392012500112 msec\nrounds: 4"
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
          "id": "3d85480377cb1362250643d2e7b553d4416ceb12",
          "message": "Merge pull request #111 from Janelia-Trackathon-2023/prune-tracking-graph\n\nPrune tracking graph API",
          "timestamp": "2024-01-10T14:47:43-05:00",
          "tree_id": "6ef987b7c05149cd961c96ef221afe3d9209ba41",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/3d85480377cb1362250643d2e7b553d4416ceb12"
        },
        "date": 1704916169219,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7477336807148622,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3373745569999755 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.856706278888814,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1672612010000023 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.3902217024485557,
            "unit": "iter/sec",
            "range": "stddev: 0.0024371439889245695",
            "extra": "mean: 418.371232666658 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4424264152581223,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.260262872000027 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 2.2623943060567497,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 442.00959899998793 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.686479447701984,
            "unit": "iter/sec",
            "range": "stddev: 0.024872129826475145",
            "extra": "mean: 271.26151499999906 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11746477317436715,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.513190576 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.7797972341948016,
            "unit": "iter/sec",
            "range": "stddev: 0.02842263324613906",
            "extra": "mean: 264.5644562499996 msec\nrounds: 4"
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
          "id": "32de15e2e6a78c960d4a27eb7f0cb977b3dfd565",
          "message": "Merge pull request #136 from Janelia-Trackathon-2023/framebuffer\n\nChange `frame_buffer` kwarg to `max_frame_buffer`",
          "timestamp": "2024-01-11T11:21:17-08:00",
          "tree_id": "62e7765760dc89eb35e91d2eaef3ff2cd41e354f",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/32de15e2e6a78c960d4a27eb7f0cb977b3dfd565"
        },
        "date": 1705000982856,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7917143564716125,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2630818069999918 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8673344332290424,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1529577999999958 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.4083280484849583,
            "unit": "iter/sec",
            "range": "stddev: 0.006764977719031529",
            "extra": "mean: 415.22582466665386 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.44761024268648963,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.234086499 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 2.2478182080799773,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 444.8758340000154 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.646204403947264,
            "unit": "iter/sec",
            "range": "stddev: 0.020331304006517753",
            "extra": "mean: 274.2578005000027 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11794242472964236,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.478713255999992 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.7687108496954944,
            "unit": "iter/sec",
            "range": "stddev: 0.02987515980558008",
            "extra": "mean: 265.34272324999364 msec\nrounds: 4"
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
          "id": "9103c93e3bfafa272116eea1ecda76f2579034eb",
          "message": "Merge pull request #142 from Janelia-Trackathon-2023/pyarrow_dependency\n\nAdd pyarrow to pyproject",
          "timestamp": "2024-01-31T11:57:02-05:00",
          "tree_id": "18e98fdc65ee53fd08c07ca127a250b63cb1cca1",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/9103c93e3bfafa272116eea1ecda76f2579034eb"
        },
        "date": 1706720327762,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7887035436350088,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2679035209999938 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.863196988365098,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1584841159999968 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.4392222924792395,
            "unit": "iter/sec",
            "range": "stddev: 0.005204677621323579",
            "extra": "mean: 409.9667353333321 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.443642148771929,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.254068966999995 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 2.0025258098342475,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 499.36934400000155 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.892204175425113,
            "unit": "iter/sec",
            "range": "stddev: 0.029699301816843375",
            "extra": "mean: 256.923828999998 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11775474820063087,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.492226557999999 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.848948312160316,
            "unit": "iter/sec",
            "range": "stddev: 0.032944105095292046",
            "extra": "mean: 259.81123125000494 msec\nrounds: 4"
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
          "id": "f4398e893f9858f6c12df51d0eea657a23b8f988",
          "message": "Merge pull request #140 from Janelia-Trackathon-2023/dependabot/github_actions/actions/cache-4\n\nci(dependabot): bump actions/cache from 3 to 4",
          "timestamp": "2024-02-02T16:34:56-05:00",
          "tree_id": "d9be1f8de0940edaf49e8d95b0738ad5b6384bc4",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/f4398e893f9858f6c12df51d0eea657a23b8f988"
        },
        "date": 1706909804666,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8053940623007345,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2416282249999995 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.864422547416895,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1568416429999928 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.381142411235138,
            "unit": "iter/sec",
            "range": "stddev: 0.003546245531461047",
            "extra": "mean: 419.9664813333375 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.4374445330448024,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.2860041089999896 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.9772219718499249,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 505.76010899999346 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.8332624151036576,
            "unit": "iter/sec",
            "range": "stddev: 0.031448174460235734",
            "extra": "mean: 260.87439150000336 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11705616648374537,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.54290747799999 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.73876545146003,
            "unit": "iter/sec",
            "range": "stddev: 0.03852088441112094",
            "extra": "mean: 267.4679685000001 msec\nrounds: 4"
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
          "id": "894a5b6000a36547815352759a57c87d05f96636",
          "message": "Merge pull request #139 from Janelia-Trackathon-2023/fix-matcher-for-empty-frame\n\nFix CTC matching for emtpy frames",
          "timestamp": "2024-02-05T10:56:34-05:00",
          "tree_id": "2bc369958255cb448d0aaaf686b6efadfdec03d8",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/894a5b6000a36547815352759a57c87d05f96636"
        },
        "date": 1707148714928,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7790003170725976,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2836965250000105 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.863275041123575,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1583793719999989 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.399576261707513,
            "unit": "iter/sec",
            "range": "stddev: 0.004922482581942421",
            "extra": "mean: 416.74024533332005 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.42703974006241174,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.3417024370000092 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 2.2027923357813965,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 453.96925700001134 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.693112898872168,
            "unit": "iter/sec",
            "range": "stddev: 0.025518704704667026",
            "extra": "mean: 270.7742837500007 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11098699329596602,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.010064785999987 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.81337784887586,
            "unit": "iter/sec",
            "range": "stddev: 0.03438722455887047",
            "extra": "mean: 262.2347010000041 msec\nrounds: 4"
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
          "id": "88752c4af00bfe6596ce30d6ec9af593603d1899",
          "message": "Merge pull request #143 from Janelia-Trackathon-2023/dependabot/github_actions/codecov/codecov-action-4\n\nci(dependabot): bump codecov/codecov-action from 3 to 4",
          "timestamp": "2024-02-05T12:49:43-05:00",
          "tree_id": "cb82537b58235a9cc231a53a6ae95bb4f57ccf30",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/88752c4af00bfe6596ce30d6ec9af593603d1899"
        },
        "date": 1707155491394,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7790533883697752,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2836090760000047 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8394668531241143,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.191232264000007 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.2674824741082853,
            "unit": "iter/sec",
            "range": "stddev: 0.005965934018778224",
            "extra": "mean: 441.01774166667457 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.41767021647006614,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.3942334419999725 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 2.1136139844513124,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 473.1232890000001 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.577759611921863,
            "unit": "iter/sec",
            "range": "stddev: 0.030470604174907965",
            "extra": "mean: 279.50452475000986 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11755557933981872,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.506614535999972 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.6060858674295764,
            "unit": "iter/sec",
            "range": "stddev: 0.04056788672563926",
            "extra": "mean: 277.30898175001073 msec\nrounds: 4"
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
          "id": "4c729d2299a7304ddfb0a9e99f1e2e7a5dd4a26c",
          "message": "Merge pull request #144 from Janelia-Trackathon-2023/pre-commit-ci-update-config\n\nci(pre-commit.ci): autoupdate",
          "timestamp": "2024-02-06T11:02:13-05:00",
          "tree_id": "6e55bd57b103350902058a3bbfb23f28288b521f",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/4c729d2299a7304ddfb0a9e99f1e2e7a5dd4a26c"
        },
        "date": 1707235447026,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8062955030397794,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2402400810000103 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8480841787730313,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.179128234000018 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.277760248008335,
            "unit": "iter/sec",
            "range": "stddev: 0.00026900939322647353",
            "extra": "mean: 439.0277690000062 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.45011117165296044,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 2.2216733620000184 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 2.0486790396173373,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 488.11940799998865 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.8752103484764047,
            "unit": "iter/sec",
            "range": "stddev: 0.030267643053454713",
            "extra": "mean: 258.0505082500011 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.1184011499248503,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.445863917999986 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.8643821105591045,
            "unit": "iter/sec",
            "range": "stddev: 0.03383164648810717",
            "extra": "mean: 258.773581749999 msec\nrounds: 4"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "46b99883e335eee0b0ded2c7175e5bdc7762d81f",
          "message": "Speed up CTCMatcher (#148)\n\nFor obtaining single-frame segmentation-label to node id mappings, it is faster (notably for larger graphs) to only get the node attribute dictionaries for the nodes present in the needed frame.\r\n\r\nFor example for PhC-C2DL-PSC, this leads to a ~3x speedup for matching.",
          "timestamp": "2024-04-12T15:46:56+02:00",
          "tree_id": "065817d39a8805f84a096c09d030dc2e37e92c79",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/46b99883e335eee0b0ded2c7175e5bdc7762d81f"
        },
        "date": 1712929722954,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7676735823431816,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.302636984000003 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8544514512767277,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.170341508000007 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.1789482993136433,
            "unit": "iter/sec",
            "range": "stddev: 0.02193829959276365",
            "extra": "mean: 458.937001999999 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5772179143945814,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7324479629999985 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8240717159041004,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 548.2240589999776 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.6875063593352624,
            "unit": "iter/sec",
            "range": "stddev: 0.03367711156809014",
            "extra": "mean: 271.18597299999436 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11710340885176387,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.539461060999997 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.639406451458339,
            "unit": "iter/sec",
            "range": "stddev: 0.041310574731282836",
            "extra": "mean: 274.7700794999943 msec\nrounds: 4"
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
          "id": "4022364e5bceb657af6f3e661c8a92890c5dcf35",
          "message": "Merge Remove support for python 3.8 (#151)",
          "timestamp": "2024-08-02T13:07:48-07:00",
          "tree_id": "84ee0cc03f6036472790000c903908ac9f748f1a",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/4022364e5bceb657af6f3e661c8a92890c5dcf35"
        },
        "date": 1722629748346,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8014190496303351,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2477866609999637 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8884075117935963,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1256095730000197 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.491451783254961,
            "unit": "iter/sec",
            "range": "stddev: 0.0025571638469003245",
            "extra": "mean: 401.3724073333454 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5936303615363975,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6845499569999447 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.9565363740227104,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 511.1072879999483 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.6176555555259777,
            "unit": "iter/sec",
            "range": "stddev: 0.02783891900401128",
            "extra": "mean: 276.4221150000026 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11875660578721019,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.420584213999973 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.768824716491095,
            "unit": "iter/sec",
            "range": "stddev: 0.03647174655392102",
            "extra": "mean: 265.3347064999707 msec\nrounds: 4"
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
          "id": "8627e36aed0de9cd2260d68ad0d3d82866c8616d",
          "message": "Merge pull request #146 from Janelia-Trackathon-2023/pre-commit-ci-update-config\n\nci(pre-commit.ci): autoupdate",
          "timestamp": "2024-08-02T16:40:59-04:00",
          "tree_id": "fcaedc5045b53feba6ff4f4fe0fba2d3d188e771",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/8627e36aed0de9cd2260d68ad0d3d82866c8616d"
        },
        "date": 1722631374200,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8052596623557713,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2418354560000182 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8965797306917438,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1153497739999807 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.523074464230802,
            "unit": "iter/sec",
            "range": "stddev: 0.0020133560691259064",
            "extra": "mean: 396.34184966667857 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5982372909506805,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6715775079999844 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.9546832872605235,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 511.5918299999862 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.5964272246789326,
            "unit": "iter/sec",
            "range": "stddev: 0.024490610871068214",
            "extra": "mean: 278.05372875000245 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11331850579420341,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.824683956000001 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.6898834434267944,
            "unit": "iter/sec",
            "range": "stddev: 0.03545546572970272",
            "extra": "mean: 271.0112704999972 msec\nrounds: 4"
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
          "id": "5d62111e8a6817a30746a3b4905c612edbf6d2cf",
          "message": "Merge pull request #145 from Janelia-Trackathon-2023/dependabot/github_actions/softprops/action-gh-release-2\n\nci(dependabot): bump softprops/action-gh-release from 1 to 2",
          "timestamp": "2024-08-02T16:46:41-04:00",
          "tree_id": "d97b5134955e178459b7fcc97970a9b7b7dff1a3",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/5d62111e8a6817a30746a3b4905c612edbf6d2cf"
        },
        "date": 1722631702931,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8504019160181144,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1759145659999888 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8967013503844381,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1151984990000017 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.553039502031299,
            "unit": "iter/sec",
            "range": "stddev: 0.0003716852139347667",
            "extra": "mean: 391.68998333334076 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5911478073836833,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.691624307000012 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 2.0509378302907084,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 487.5818200000026 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.7740861648308024,
            "unit": "iter/sec",
            "range": "stddev: 0.02607270683706954",
            "extra": "mean: 264.9648037500043 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11911657150432468,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.395137530999989 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.8916296982844196,
            "unit": "iter/sec",
            "range": "stddev: 0.03282174779445161",
            "extra": "mean: 256.96175574999813 msec\nrounds: 4"
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
          "id": "ffe7cb1dab76bbce7e2fe2f900a6f4d26050df51",
          "message": "Merge pull request #150 from Janelia-Trackathon-2023/iou-1-to-1\n\nAdd iou matcher option to use linear assignment to get one-to-one matching",
          "timestamp": "2024-08-02T13:50:25-07:00",
          "tree_id": "d7de93aa9cca7c45fec3498e971a3328230df6ba",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/ffe7cb1dab76bbce7e2fe2f900a6f4d26050df51"
        },
        "date": 1722631945967,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7656031219696625,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.3061597730000187 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8948417772804906,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1175159959999803 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.4584890455271644,
            "unit": "iter/sec",
            "range": "stddev: 0.004972455192621238",
            "extra": "mean: 406.75389700000625 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5784060639096876,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7288892050000015 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.7805941205483637,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 561.6103010000018 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.8166613369853826,
            "unit": "iter/sec",
            "range": "stddev: 0.03594179856132511",
            "extra": "mean: 262.0090994999984 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11957937733517968,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.362645987000008 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.658338249896093,
            "unit": "iter/sec",
            "range": "stddev: 0.0430451042060616",
            "extra": "mean: 273.34815199999696 msec\nrounds: 4"
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
          "id": "280308d3b30cc9b76cc6b2f44fb5860d43118487",
          "message": "Merge pull request #153 from Janelia-Trackathon-2023/bugfix_iou\n\nFix multiple IOU-related bugs",
          "timestamp": "2024-08-05T16:04:24-04:00",
          "tree_id": "bb0ef4cb6960f62ca19ca8cff083347217942a56",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/280308d3b30cc9b76cc6b2f44fb5860d43118487"
        },
        "date": 1722888394543,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.747738820608491,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.337365363999993 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8686030461590855,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1512738810000087 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.420037753847385,
            "unit": "iter/sec",
            "range": "stddev: 0.004302257873694319",
            "extra": "mean: 413.21669399999905 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5804944393546416,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7226693870000531 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.9068236787488226,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 524.4323379999969 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.71196193225662,
            "unit": "iter/sec",
            "range": "stddev: 0.034809248748145095",
            "extra": "mean: 269.3993144999922 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11165354397651546,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.956276392000007 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.568703324761905,
            "unit": "iter/sec",
            "range": "stddev: 0.049734147323187754",
            "extra": "mean: 280.21382250000215 msec\nrounds: 4"
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
          "id": "599aa8e250e638d25f17dd19cbe013a74159e8e6",
          "message": "Merge pull request #141 from Janelia-Trackathon-2023/check_empty_subgraph\n\nCheck empty subgraph",
          "timestamp": "2024-08-06T13:09:23-04:00",
          "tree_id": "881cc375ea701969471d2e232b1ffa1a2dfc1660",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/599aa8e250e638d25f17dd19cbe013a74159e8e6"
        },
        "date": 1722964263154,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.840896791436604,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.189206583000015 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8950697937474195,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1172313120000013 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.4590866426948126,
            "unit": "iter/sec",
            "range": "stddev: 0.006112280474474288",
            "extra": "mean: 406.65504933333335 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5882896091669961,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.699843044000005 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.972770040570345,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 506.90145300001177 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.799625697732578,
            "unit": "iter/sec",
            "range": "stddev: 0.03530472653035524",
            "extra": "mean: 263.1838185000035 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11779984631905056,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.48897542100002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.7321987508844563,
            "unit": "iter/sec",
            "range": "stddev: 0.03816582947056304",
            "extra": "mean: 267.93857100000906 msec\nrounds: 4"
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
          "id": "9475cb2d32b79093fe09fb050287dbc548e1f6e3",
          "message": "Merge pull request #154 from Janelia-Trackathon-2023/pre-commit-ci-update-config\n\nci(pre-commit.ci): autoupdate",
          "timestamp": "2024-08-06T13:12:38-04:00",
          "tree_id": "8ff638730166a79a4f4a885c9231d1dc82d51d8c",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/9475cb2d32b79093fe09fb050287dbc548e1f6e3"
        },
        "date": 1722964456948,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8546602269294917,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1700556179999921 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.9012974271099431,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1095116550000057 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.528464375232024,
            "unit": "iter/sec",
            "range": "stddev: 0.004383368951366354",
            "extra": "mean: 395.4969703333215 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.6017232622535529,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6618935359999796 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.97699669059249,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 505.81774100001553 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.8154940220341675,
            "unit": "iter/sec",
            "range": "stddev: 0.03301453868316172",
            "extra": "mean: 262.08925875000233 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.11917785258977104,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 8.390820762999965 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.7217298851722243,
            "unit": "iter/sec",
            "range": "stddev: 0.03871818738033638",
            "extra": "mean: 268.6922562500058 msec\nrounds: 4"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "4160403789bc4401e954cc28783da608efdf7df3",
          "message": "Speed up IoU Matcher (#156)\n\nThis commit brings the speed ups already in place in the CTC matcher to\r\nthe IoU matcher. It calculates the IoU on local crops instead of full\r\nlabel images.",
          "timestamp": "2024-08-14T16:00:27+02:00",
          "tree_id": "b12dbf5c41b7b5dc30efc482c65a33e705a71676",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/4160403789bc4401e954cc28783da608efdf7df3"
        },
        "date": 1723644120108,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8158418213373478,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2257277990000262 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8555035693127526,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.168902194999987 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.3352539247813224,
            "unit": "iter/sec",
            "range": "stddev: 0.003393657288788132",
            "extra": "mean: 428.21895699999385 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.565760838510801,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.767531316999964 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8380180768710448,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 544.0642899999943 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.6921428489220736,
            "unit": "iter/sec",
            "range": "stddev: 0.03599064605093471",
            "extra": "mean: 270.84542524998767 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.556811103034329,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7959411990000262 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.4834677244844765,
            "unit": "iter/sec",
            "range": "stddev: 0.038155637820505746",
            "extra": "mean: 287.07026420001966 msec\nrounds: 5"
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
          "id": "2f38c1b89d0f51ba6ff13c7a24f3aaebe65ee17e",
          "message": "Merge pull request #160 from Janelia-Trackathon-2023/release-notes\n\nGroup PRs in release notes based on labels",
          "timestamp": "2024-09-16T12:02:04-07:00",
          "tree_id": "b6d88a151366c11d38d790ac2f13426b8f150910",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/2f38c1b89d0f51ba6ff13c7a24f3aaebe65ee17e"
        },
        "date": 1726513405231,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8183151740958517,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2220230439999966 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8810784790372477,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1349726770000075 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.444471089179266,
            "unit": "iter/sec",
            "range": "stddev: 0.00440838388216874",
            "extra": "mean: 409.0864500000085 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5577083827248006,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7930517650000013 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.818799551954739,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 549.813198999999 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.5342691925591203,
            "unit": "iter/sec",
            "range": "stddev: 0.04301793205532706",
            "extra": "mean: 282.94392575001126 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.5359016929287209,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.866013885000001 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.6601664273464056,
            "unit": "iter/sec",
            "range": "stddev: 0.0397589261616889",
            "extra": "mean: 273.21162025000945 msec\nrounds: 4"
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
          "id": "6f7191051b05a51e2229657cb64c2c8328899309",
          "message": "Merge pull request #159 from Janelia-Trackathon-2023/templates\n\nReduce number of checkboxes in issue and PR templates",
          "timestamp": "2024-09-16T12:06:30-07:00",
          "tree_id": "2b445736ce7fffb6cfb04f27b7c1563b63911cdd",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/6f7191051b05a51e2229657cb64c2c8328899309"
        },
        "date": 1726513675943,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.8260237732450366,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.210618910000008 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8765435728521538,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.140844598000001 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.561494174880483,
            "unit": "iter/sec",
            "range": "stddev: 0.002058230842628897",
            "extra": "mean: 390.39713999999987 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5823265773991426,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7172494590000014 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.929283759134388,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 518.3270710000016 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.6943621600698155,
            "unit": "iter/sec",
            "range": "stddev: 0.03249940063741546",
            "extra": "mean: 270.6827205000124 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.5487816645065426,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.8222183149999864 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.6078265971384527,
            "unit": "iter/sec",
            "range": "stddev: 0.0373666461339545",
            "extra": "mean: 277.1751837500034 msec\nrounds: 4"
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
          "id": "ba122c779d534307c922a8705960c60dede9aa54",
          "message": "Merge pull request #155 from Janelia-Trackathon-2023/bugfix_frame_buffer\n\nFix frame buffer bug where predecessors were not checked properly",
          "timestamp": "2024-09-16T12:09:37-07:00",
          "tree_id": "b880ea5e71dfc13e8dfb377d845495bd568820a5",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/ba122c779d534307c922a8705960c60dede9aa54"
        },
        "date": 1726513861298,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7976554042490982,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2536741989999882 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8694434665765526,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1501610379999931 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.511843907093604,
            "unit": "iter/sec",
            "range": "stddev: 0.0045034810925761",
            "extra": "mean: 398.1139103333362 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5656339828969151,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7679277240000033 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8650917861465497,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 536.166642000012 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.633862145126041,
            "unit": "iter/sec",
            "range": "stddev: 0.04249957967983197",
            "extra": "mean: 275.18930550000675 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.5615815517989288,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7806852749999962 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.709744985628287,
            "unit": "iter/sec",
            "range": "stddev: 0.0346346738205875",
            "extra": "mean: 269.5603077500053 msec\nrounds: 4"
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
          "id": "ab3cccf18542a072eeff22373b0a47fb71897d19",
          "message": "Merge pull request #116 from Janelia-Trackathon-2023/docs-metrics-pages\n\nAdd written documentation for errors and metrics",
          "timestamp": "2024-09-18T10:20:12-07:00",
          "tree_id": "7a1493c85ea4c3f233694e414cf021a6ed914c81",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/ab3cccf18542a072eeff22373b0a47fb71897d19"
        },
        "date": 1726680091275,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_data",
            "value": 0.7906470076989875,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.2647869280000066 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_data",
            "value": 0.8379739745461743,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1933544840000252 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks",
            "value": 2.254168976194308,
            "unit": "iter/sec",
            "range": "stddev: 0.023794393956266757",
            "extra": "mean: 443.62246599999366 msec\nrounds: 3"
          },
          {
            "name": "tests/bench.py::test_ctc_matched",
            "value": 0.5769456305044343,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.7332655749999901 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics",
            "value": 1.8249332016962134,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 547.9652620000195 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_div_metrics",
            "value": 3.6753524770987958,
            "unit": "iter/sec",
            "range": "stddev: 0.03926560942936718",
            "extra": "mean: 272.0827475000078 msec\nrounds: 4"
          },
          {
            "name": "tests/bench.py::test_iou_matched",
            "value": 0.5506125294590093,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.8161591799999997 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics",
            "value": 3.5539784199783084,
            "unit": "iter/sec",
            "range": "stddev: 0.043454480986479645",
            "extra": "mean: 281.37480924999636 msec\nrounds: 4"
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
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "b5adc6817d8f0c19c571e1d9ef01e2ab8801b500",
          "message": "Merge pull request #167 from Janelia-Trackathon-2023/fix-benchmark-report\n\nAdd data download to benchmark report action",
          "timestamp": "2024-11-14T17:24:46+01:00",
          "tree_id": "fce4a3a13cfd3063b668b34140483defe7a2dd27",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/b5adc6817d8f0c19c571e1d9ef01e2ab8801b500"
        },
        "date": 1731602071408,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.1632457191414743,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 6.125734905999991 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.06048659603035379,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.53258846799997 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8683362158405495,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1516276549999702 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3534921241179643,
            "unit": "iter/sec",
            "range": "stddev: 0.005615308897691673",
            "extra": "mean: 738.8295670000105 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10209192842130888,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.795093651999991 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6905769554865047,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4480645379999828 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.05940877977258453,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.832528858999922 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.6760592615303413,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 272.0304350000333 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.2907263361477307,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.4396608619999824 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6356871573924834,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.573100838000073 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05616017315614575,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.806212905000052 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.362883836487578,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 74.83414599994376 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3616955321858362,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 734.3785570000136 msec\nrounds: 1"
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
          "id": "a78b48c58bbdc76a7eccfc266cd8b747eb4f8e1d",
          "message": "Merge pull request #170 from Janelia-Trackathon-2023/matcher-metric-val\n\nMetrics validate that the matcher is supported",
          "timestamp": "2024-11-26T14:55:35-05:00",
          "tree_id": "5257188a6330fd67ef15ffc1adcff84b45d168df",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/a78b48c58bbdc76a7eccfc266cd8b747eb4f8e1d"
        },
        "date": 1732651660378,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.16326719892906466,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 6.124928991000047 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.059375550858528546,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.841949010000008 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8590748268391766,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1640429550000135 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3399006051414495,
            "unit": "iter/sec",
            "range": "stddev: 0.0005469845718583158",
            "extra": "mean: 746.3240154999653 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10224861748560383,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.780083336000075 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6797935873391756,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.471034765000013 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.0591853041230782,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.896086195999942 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.5707122865440524,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 280.05616799998734 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.27639947005332816,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.6179519439999694 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6360722253091611,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.572148507999941 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05616003433471741,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.80625692000001 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.599681647779569,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 73.53113299996039 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.360754112620353,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 734.8866270000372 msec\nrounds: 1"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "66853113+pre-commit-ci[bot]@users.noreply.github.com",
            "name": "pre-commit-ci[bot]",
            "username": "pre-commit-ci[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "f0584edd406dfb69c5fd9b12863d9782fb2691da",
          "message": "ci(pre-commit.ci): autoupdate (#158)\n\n* ci(pre-commit.ci): autoupdate\r\n\r\nupdates:\r\n- [github.com/crate-ci/typos: v1.23.6 → typos-dict-v0.11.37](https://github.com/crate-ci/typos/compare/v1.23.6...typos-dict-v0.11.37)\r\n- [github.com/astral-sh/ruff-pre-commit: v0.5.6 → v0.8.1](https://github.com/astral-sh/ruff-pre-commit/compare/v0.5.6...v0.8.1)\r\n- [github.com/psf/black: 24.8.0 → 24.10.0](https://github.com/psf/black/compare/24.8.0...24.10.0)\r\n- [github.com/abravalheri/validate-pyproject: v0.18 → v0.23](https://github.com/abravalheri/validate-pyproject/compare/v0.18...v0.23)\r\n- [github.com/pre-commit/mirrors-mypy: v1.11.1 → v1.13.0](https://github.com/pre-commit/mirrors-mypy/compare/v1.11.1...v1.13.0)\r\n\r\n* style(pre-commit.ci): auto fixes [...]\r\n\r\n---------\r\n\r\nCo-authored-by: pre-commit-ci[bot] <66853113+pre-commit-ci[bot]@users.noreply.github.com>",
          "timestamp": "2024-12-03T11:40:51-05:00",
          "tree_id": "1e2aca18cdba887ce9ba9cd955c0b67847de2738",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/f0584edd406dfb69c5fd9b12863d9782fb2691da"
        },
        "date": 1733244428796,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.16761540460901375,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.966038756000017 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.058280505654749855,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.158396084000003 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8465728530243279,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1812332470000229 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3312208766105151,
            "unit": "iter/sec",
            "range": "stddev: 0.0031108208244432054",
            "extra": "mean: 751.1901424999792 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10132708454499006,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.869029632999968 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6764541688423078,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4782967510000162 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.059197875811904485,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.892498020999994 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.535611426065509,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 282.83651099997087 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.23899916823031453,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.184114980000004 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6260826538204145,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5972331990000157 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05574864192458829,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.937656693999998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 12.392523516204793,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 80.69381500001782 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3343018532346582,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 749.4556030000012 msec\nrounds: 1"
          }
        ]
      },
      {
        "commit": {
          "author": {
            "email": "49699333+dependabot[bot]@users.noreply.github.com",
            "name": "dependabot[bot]",
            "username": "dependabot[bot]"
          },
          "committer": {
            "email": "noreply@github.com",
            "name": "GitHub",
            "username": "web-flow"
          },
          "distinct": true,
          "id": "369b29469f104d8c976d1adbff40a7cbed97d832",
          "message": "ci(dependabot): bump codecov/codecov-action from 4 to 5 (#168)\n\nBumps [codecov/codecov-action](https://github.com/codecov/codecov-action) from 4 to 5.\r\n- [Release notes](https://github.com/codecov/codecov-action/releases)\r\n- [Changelog](https://github.com/codecov/codecov-action/blob/main/CHANGELOG.md)\r\n- [Commits](https://github.com/codecov/codecov-action/compare/v4...v5)\r\n\r\n---\r\nupdated-dependencies:\r\n- dependency-name: codecov/codecov-action\r\n  dependency-type: direct:production\r\n  update-type: version-update:semver-major\r\n...\r\n\r\nSigned-off-by: dependabot[bot] <support@github.com>\r\nCo-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>\r\nCo-authored-by: Morgan Schwartz <msschwartz21@gmail.com>",
          "timestamp": "2024-12-03T12:50:06-05:00",
          "tree_id": "901c3aa755b06c22c9261d8f28e611c5af15f806",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/369b29469f104d8c976d1adbff40a7cbed97d832"
        },
        "date": 1733248537381,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.1705511427340492,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.863343885999996 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.05916939008271161,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.900630522 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8510610680035171,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1750038130000178 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.340952746631447,
            "unit": "iter/sec",
            "range": "stddev: 0.0019320660419939787",
            "extra": "mean: 745.7384330000139 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10012582102035598,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.987433708999959 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6834957000721532,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4630669950000197 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.05888201972058093,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.983113091999996 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.7511730621515995,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 266.5832749999595 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.24310177851411,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.1135034310000265 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6342451783027695,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.576677339000014 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.056055814828189554,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.839362483000002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.593120521712212,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 73.56662499995537 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3727542843259652,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 728.4624870000016 msec\nrounds: 1"
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
          "id": "6212b53c87627d209f65695b937ca271c26a8156",
          "message": "Merge pull request #171 from Janelia-Trackathon-2023/unit_tests\n\nCanonical unit test examples: Segmentations for matching, and matched graphs without divisions",
          "timestamp": "2024-12-09T15:47:12-05:00",
          "tree_id": "c8435c3858f60ad7ba20a11302e529e3c2b60513",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/6212b53c87627d209f65695b937ca271c26a8156"
        },
        "date": 1733777567522,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.17550905290701008,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.697711789999971 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.05215236591256234,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 19.174585515000047 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.9096305722359985,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.0993473949999952 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3196597509651362,
            "unit": "iter/sec",
            "range": "stddev: 0.0062149241344017095",
            "extra": "mean: 757.7710839999838 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.09809719743895727,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 10.193971143999988 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6792460148616049,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4722206359999745 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.05927232442152023,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.87128031100002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.3247010462897832,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 300.77892299999576 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.24024867615766146,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.16235384099997 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6445431368609117,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.551486538000006 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05598483288780908,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.861980619000008 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.95667744043681,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 71.650290999969 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3970919335810321,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 715.7725099999652 msec\nrounds: 1"
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
          "id": "48351ed9eaec5075e940fea1914d2de3cbe40448",
          "message": "Merge pull request #172 Add tests cases to docs using example notebook",
          "timestamp": "2024-12-17T11:00:04-05:00",
          "tree_id": "6235ac9a0e4921874aa789e33148a53f322494e0",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/48351ed9eaec5075e940fea1914d2de3cbe40448"
        },
        "date": 1734451871700,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.17150621821297288,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.830692381999938 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.06094021889119028,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.409524255000065 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8587140799074054,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.164531970999974 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.324224826777263,
            "unit": "iter/sec",
            "range": "stddev: 0.0039152636825606",
            "extra": "mean: 755.1587764999681 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10392187146719611,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.62261346799994 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6487565324414526,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5414102979999598 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.058636989258310124,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.054081606999944 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.811499095334893,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 262.3639610000055 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.25406187998119983,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.9360489659999303 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6332706111511948,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5791037550000055 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05539840417252884,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.051061487000084 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 14.188243485236955,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 70.48088800002006 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.415476910315246,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 706.4756710000211 msec\nrounds: 1"
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
          "id": "af21f3ee992d2a6bf49d7f3407c4a602f2fb8b30",
          "message": "Merge pull request #173 Test the IOU matcher using standardized segmentation test cases",
          "timestamp": "2024-12-18T15:27:49-05:00",
          "tree_id": "9ab83cb6835b6754ce5d101c90978a79c2822928",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/af21f3ee992d2a6bf49d7f3407c4a602f2fb8b30"
        },
        "date": 1734553995750,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.17547657645672388,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.6987662980000096 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.05198832299967722,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 19.23508861800002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8734604621727999,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1448715120000088 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3494822837395335,
            "unit": "iter/sec",
            "range": "stddev: 0.0011984144722225307",
            "extra": "mean: 741.0249189999831 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10208223212976147,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.796024039999963 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6645681982121401,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.504736462999972 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.05886325463300865,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.988527159 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.3945766213940725,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 294.5875469999919 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.24433713958699546,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.092705684000009 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6290501658341987,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5896983330000012 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05578009308001936,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.927542690999985 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 12.813315515484177,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 78.04381299996521 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.408003349831437,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 710.2255830000104 msec\nrounds: 1"
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
          "id": "68d63ad2bf387b8b75a338b326f58f8152e90771",
          "message": "Merge pull request #175 Add standard division test cases",
          "timestamp": "2024-12-18T16:12:40-05:00",
          "tree_id": "7f99c9112de3d38b2470eea8d6739bc0097fa0d5",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/68d63ad2bf387b8b75a338b326f58f8152e90771"
        },
        "date": 1734556682439,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.1814181159500801,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.512128679999989 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.05228684290607731,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 19.125270228999995 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8949902970924662,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1173305490000018 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3546728067879967,
            "unit": "iter/sec",
            "range": "stddev: 0.00037633283556411605",
            "extra": "mean: 738.1856304999985 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10354352533679813,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.657774320000016 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6438290344242094,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5532073679999883 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.0582124875854303,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.178444719999987 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.6754855445967056,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 272.0728969999868 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.24219765433533702,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.1288591449999785 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6065641612903263,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6486302090000322 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.054717837306721584,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.275576105000027 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.620835203192017,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 73.41693699999041 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3789731392952311,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 725.1772870000082 msec\nrounds: 1"
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
          "id": "2ce238f880d22fa3df62d432c0257fb5a5f8ae5f",
          "message": "Merge pull request #177 Test division errors using standard test cases",
          "timestamp": "2024-12-19T15:51:33-05:00",
          "tree_id": "88813e7a02bfcc29532513ec109a54650b85b9ca",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/2ce238f880d22fa3df62d432c0257fb5a5f8ae5f"
        },
        "date": 1734641829156,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.18054186288203752,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.53888158700002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.05215621148200062,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 19.17317173899997 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.89505340572438,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.117251768000017 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.337265505495556,
            "unit": "iter/sec",
            "range": "stddev: 0.0010435920282600131",
            "extra": "mean: 747.7946570000142 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10390995915829382,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.623716610999963 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6769675713144933,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4771756320000122 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.05946913364127784,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.815445909000005 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.6798646816607254,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 271.7491230000064 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.23967893026584253,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.172248260999993 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6384593499849632,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5662704289999851 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05589191705588319,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.891674729999977 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.174970885944372,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 75.9014960000286 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3972836077284236,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 715.6743229999734 msec\nrounds: 1"
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
          "id": "69ffb71a093b968aef4a316354007e421b8df28a",
          "message": "Add written documentation for the ctc error types with example graphs (#178)\n\n* Add written documentation for the ctc error types with example graphs\n\n* Add matplotlib as dependency for new plots in the docs\n\n* Fix path to import of example graphs\n\n* Try different path configuration for rtd build\n\n* Try path with two ../\n\n* Correct imports with two ../\n\n* Draga's edits from code review\n\nCo-authored-by: Draga Doncila Pop <17995243+DragaDoncila@users.noreply.github.com>\n\n---------\n\nCo-authored-by: Draga Doncila Pop <17995243+DragaDoncila@users.noreply.github.com>",
          "timestamp": "2025-01-07T13:14:29-05:00",
          "tree_id": "471247f5959d94d0664391f25bf6d28fda386ba2",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/69ffb71a093b968aef4a316354007e421b8df28a"
        },
        "date": 1736274329989,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.16705401785267726,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.986087690999966 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.05890746967651795,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.97577583100002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8424472946312228,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.187017878000006 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.259848464582615,
            "unit": "iter/sec",
            "range": "stddev: 0.006704898929159567",
            "extra": "mean: 793.7462544999789 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.0948270591499265,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 10.545513158000063 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6388448262705881,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5653253479999876 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.058703985434229125,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.03461856299998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.1878725371760672,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 313.6888279999539 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.26342011656916514,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.796217286000001 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6295153336831939,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.588523656999996 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05497647607029903,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.189598014999888 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.24057971812586,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 75.52539400001024 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.370252512667845,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 729.7924950000834 msec\nrounds: 1"
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
          "id": "b367f32072a7c0eb9c4dab9ba6ee50aeebaa7819",
          "message": "Add tests for CTC node and edge track errors (#176)\n\n* Test ctc node errors with graph test cases\n\n* Start drafting ctc edge error tests -- currently failing and incomplete\n\n* Fix obvious issues with CTC error tests\n\n* Add tests cases for non split edges and crossover/identity switch edges\n\n* Add test for two to one with edges\n\n* Add test for crossover edge\n\n* Add division test cases\n\n* Add test description back to notebook\n\n* Annotate div cases with one to one matching\n\n* Add division cases to collection of plots of test cases\n\n* Add additional context to testing non sequential ids\n\n* Correct notebook header levels\n\n* Add test cases for limits of matching in shifted division cases\n\n* Differentiate between standard test case testing and end to end tests\n\n* Add tests for intertrack edges\n\n* Update tests to reflect correct ctc behavior\n\n* Remove leftover comments and test code from ctc edge errors\n\n* Rename node/edge flags to prefix with CTC\n\n* Improve AssertionError test with explicit match\n\n* Draga's improvements/clarifications to test comments\n\nCo-authored-by: Draga Doncila Pop <17995243+DragaDoncila@users.noreply.github.com>\n\n* Improvements based on Draga's questions\n\n* Update ctc errors docs to match changes introduced in last merge\n\n* Correction to notebook for test examples\n\n---------\n\nCo-authored-by: Caroline Malin-Mayor <malinmayorc@janelia.hhmi.org>\nCo-authored-by: Draga Doncila Pop <17995243+DragaDoncila@users.noreply.github.com>",
          "timestamp": "2025-01-07T13:34:45-05:00",
          "tree_id": "e25113db496b9928d6d259c9a824ac01e7600aa5",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/b367f32072a7c0eb9c4dab9ba6ee50aeebaa7819"
        },
        "date": 1736275228670,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.18145758679429064,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.510929675999989 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.05119508112287133,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 19.533126583000012 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8706866178422035,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1485188579999885 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3547966642622078,
            "unit": "iter/sec",
            "range": "stddev: 0.0011074628624909242",
            "extra": "mean: 738.1181444999925 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10201018698719759,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.802942524999992 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6644210126762566,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5050697989999549 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.05909931903307254,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.920668738000018 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.656214354195123,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 273.5069400000043 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.21854567581524123,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.575702522000029 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6385533491119338,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.566039864000004 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.055614091865160455,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.98105419799998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.671333914234385,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 73.14575200001627 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3873058091814048,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 720.821605000026 msec\nrounds: 1"
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
          "id": "fd11de3d30cb6ed88750ed76db15b381ee82a0c0",
          "message": "Update the test case notebook with py:percent files (#180)\n\n* Test ctc node errors with graph test cases\n\n* Start drafting ctc edge error tests -- currently failing and incomplete\n\n* Fix obvious issues with CTC error tests\n\n* Add tests cases for non split edges and crossover/identity switch edges\n\n* Add test for two to one with edges\n\n* Add test for crossover edge\n\n* Add division test cases\n\n* Add test description back to notebook\n\n* Annotate div cases with one to one matching\n\n* Add division cases to collection of plots of test cases\n\n* Add additional context to testing non sequential ids\n\n* Correct notebook header levels\n\n* Add test cases for limits of matching in shifted division cases\n\n* Differentiate between standard test case testing and end to end tests\n\n* Add tests for intertrack edges\n\n* Update tests to reflect correct ctc behavior\n\n* Remove leftover comments and test code from ctc edge errors\n\n* Rename node/edge flags to prefix with CTC\n\n* Replace the test case notebook with three py:percent files\n\n* Remove old test case example notebook\n\n* Add jupytext as docs dependency\n\n* Add ipykernel as a docs dependency for running notebooks during docs build\n\n* Add matplotlib as dependency for docs\n\n* Try a different path for sys appending path to examples tests\n\n* Correct path to get jupyter-execute blocks to run\n\n* Try conditional path depending on local vs rtd\n\n* Try path based on calling from docs/source\n\n* Correct intro text on test case files\n\n* Make plot names more consistent\n\n* Add landing page for test cases\n\n---------\n\nCo-authored-by: Caroline Malin-Mayor <malinmayorc@janelia.hhmi.org>",
          "timestamp": "2025-01-14T14:01:54-05:00",
          "tree_id": "e0ce9938efd81276c309d40da55b3d4473038eb4",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/fd11de3d30cb6ed88750ed76db15b381ee82a0c0"
        },
        "date": 1736881645211,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.1789486420833035,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.588195519999999 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.050101675257571546,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 19.959412431999993 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.866975590703654,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1534350109999991 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3485568927155607,
            "unit": "iter/sec",
            "range": "stddev: 0.003938009893390217",
            "extra": "mean: 741.5334165000047 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10174342843507084,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.82864461500003 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6555014260977811,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5255496939999489 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.05827654236396069,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.159562998000013 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.284873143733923,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 304.42575900002566 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.22894521641072763,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.367857147999985 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.59559815417557,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.678984383999989 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05478875215695472,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.251921436999964 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.36125907740553,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 74.84324600000036 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.432234384377949,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 698.2097419999604 msec\nrounds: 1"
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
          "id": "6b0bfabdc8bee409ff0ef5859f8e9b9d17f70fb2",
          "message": "Add example graph plots for division error documentation (#189)",
          "timestamp": "2025-01-15T11:25:53-05:00",
          "tree_id": "c23594141b46bd7dc6dcd7a0cf503d52a21f0321",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/6b0bfabdc8bee409ff0ef5859f8e9b9d17f70fb2"
        },
        "date": 1736958697209,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.180949838286614,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.526393443999979 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.05260054713554241,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 19.01120909300002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8894779636575585,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1242549459999793 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3240892632843757,
            "unit": "iter/sec",
            "range": "stddev: 0.0021381600915577896",
            "extra": "mean: 755.2360914999952 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.09780283398405382,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 10.224652591999984 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6598339776156755,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5155327460000194 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.058804849957779716,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.00540007699999 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.493177783617623,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 286.27228899995316 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.23219006083492116,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.306816563999973 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6460339329530037,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5479063079999946 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05616483068085899,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.80473630700004 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 14.201416301576446,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 70.4155119999541 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.4135873301728725,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 707.4200359999736 msec\nrounds: 1"
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
          "id": "79b06ac32021bdcca511b1e971da5a8f23638ec4",
          "message": "Update node and edge annotations to be sparse (#192)\n\n* Add functions for removing node and edge flags\n\n* Remove flags when correcting shifted divisions instead of flipping to False\n\n* Make ctc node error flags sparse and update tests for new behavior\n\n* Fix error in mapping for ns vertex test\n\n* Update ctc edge flags to be sparse\n\n* Update ns error test to reflect sparse flags\n\n* Draga's docstring improvements\n\nCo-authored-by: Draga Doncila Pop <17995243+DragaDoncila@users.noreply.github.com>\n\n---------\n\nCo-authored-by: Caroline Malin-Mayor <cmalinmayor@gmail.com>\nCo-authored-by: Draga Doncila Pop <17995243+DragaDoncila@users.noreply.github.com>",
          "timestamp": "2025-01-16T11:10:03-05:00",
          "tree_id": "04803ccb827c356791b79ce0a92215a30e85561e",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/79b06ac32021bdcca511b1e971da5a8f23638ec4"
        },
        "date": 1737044135518,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.17813459797174322,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.613732600999981 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.05068927823938989,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 19.728037855999986 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8607976208600399,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1617132480000123 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3479401392778052,
            "unit": "iter/sec",
            "range": "stddev: 0.0003389233512724755",
            "extra": "mean: 741.8727070000131 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10056789071762226,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.943531607000011 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6612776129742333,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5122241860000258 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.05881065975055135,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.003720145999978 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.373354200362396,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 296.44085400002496 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.22325759624276298,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.479130908999991 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6293930545571385,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5888322769999945 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.055291550012400006,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.08594622100003 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.30896355634323,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 75.13733100000763 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.341760105610459,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 745.2897100000087 msec\nrounds: 1"
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
          "id": "cbdee0be26fdabbccdd68b3efd07dea0afcd2a95",
          "message": "Update example notebooks and run in CI (#196)\n\n* Add action to run example notebooks\n\n* Add ipykernel for notebook execution action\n\n* Correct current bugs in ctc example",
          "timestamp": "2025-01-21T12:56:45-05:00",
          "tree_id": "fc7c529d74ee940d575bcc215fcb3bf6bc3d8a48",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/cbdee0be26fdabbccdd68b3efd07dea0afcd2a95"
        },
        "date": 1737482537479,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.17860452807286917,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.598962192000016 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.05183276564264747,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 19.292815801000017 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8594619233602668,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1635186769999848 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3552592680063962,
            "unit": "iter/sec",
            "range": "stddev: 0.00042719219789042937",
            "extra": "mean: 737.8661955000041 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.1005467968887755,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.945617671999997 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.64308971951559,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.554992980999998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.0585990133759711,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.06513373499999 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.9248496324366138,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 254.7868309999899 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.23152530348689085,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.319182331000036 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6174973058469082,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.6194402639999907 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05497081993447882,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.19146960500001 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.270128243319139,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 75.35722199997963 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3928366115003354,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 717.9593010000076 msec\nrounds: 1"
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
          "id": "e4c7fede9147675d6607a142066217f2b13a621a",
          "message": "Merge pull request #199 from Janelia-Trackathon-2023/165_memory_in_ctc_loader\n\nPre-allocate numpy array and populate during reading for ctc loader",
          "timestamp": "2025-01-21T15:46:47-05:00",
          "tree_id": "e5b17be6ce693c5a9f136f4bbb05bce1fed2a8f9",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/e4c7fede9147675d6607a142066217f2b13a621a"
        },
        "date": 1737492731587,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.1788220571045506,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.592151305000016 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.060841910566546364,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 16.436038755 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.9262851796291531,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.0795811289999904 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3385282471262163,
            "unit": "iter/sec",
            "range": "stddev: 0.0087259098118801",
            "extra": "mean: 747.0892020000122 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.10040472039342717,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 9.959691098999997 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6557956471511523,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5248652599999843 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.05819045052990063,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.18495029500002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.5819187834593156,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 279.17997599996625 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.22645519914520756,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.4158844830000135 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6311780862986898,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5843389080000065 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.0547975740279081,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.248983057000032 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.129290332050775,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 76.16557900001908 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3641985957643878,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 733.031101999984 msec\nrounds: 1"
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
          "id": "239000a88bc773828f54de60fdd5cdb7778c0573",
          "message": "Merge pull request #186 from Janelia-Trackathon-2023/pre-commit-ci-update-config\n\nci(pre-commit.ci): autoupdate",
          "timestamp": "2025-01-22T12:47:56-05:00",
          "tree_id": "5cbdf309a456fe134845692c163fb72640a8c48e",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/239000a88bc773828f54de60fdd5cdb7778c0573"
        },
        "date": 1737568630050,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.1726673113176561,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.791484169 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.06617017457202594,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 15.11254891599998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.8903912630834634,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1231017659999907 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3367297015058588,
            "unit": "iter/sec",
            "range": "stddev: 0.004008715621795999",
            "extra": "mean: 748.0943969999885 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.0990458922570075,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 10.09632986500003 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6712052671893578,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.4898572000000172 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.058684896799344105,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.04015947099998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.778042011517359,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 264.6873690000007 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.28416245126660394,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 3.519113786999924 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6376804800040705,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5681834890000346 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.05532674357610635,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.074441678000085 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.085535170895652,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 76.42026000007718 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3663862513690321,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 731.85748100002 msec\nrounds: 1"
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
          "id": "d7c1ac3cd475d71e598aad4a41ec65c1d80b1546",
          "message": "Bugfix: fix testing issue with GT nodes matched to NS nodes (#200)\n\nRewrite test for gt nodes matched to NS",
          "timestamp": "2025-01-22T17:14:46-05:00",
          "tree_id": "7502799aa1066189a49195c7de9b9bb090ce3395",
          "url": "https://github.com/Janelia-Trackathon-2023/traccuracy/commit/d7c1ac3cd475d71e598aad4a41ec65c1d80b1546"
        },
        "date": 1737584409967,
        "tool": "pytest",
        "benches": [
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[2d]",
            "value": 0.18138571214250507,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 5.513113398999991 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_gt_ctc_data[3d]",
            "value": 0.06384763701467984,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 15.66228676199998 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_load_pred_ctc_data[2d]",
            "value": 0.9052687713425137,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.1046443129999943 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[2d]",
            "value": 1.3386579819998539,
            "unit": "iter/sec",
            "range": "stddev: 0.001586674785003969",
            "extra": "mean: 747.0167984999989 msec\nrounds: 2"
          },
          {
            "name": "tests/bench.py::test_ctc_checks[3d]",
            "value": 0.09847344161604579,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 10.15502234500002 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[2d]",
            "value": 0.6626241513316904,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.509151150000008 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_matcher[3d]",
            "value": 0.058526683183223495,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 17.08622367800004 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[2d]",
            "value": 3.631200122606989,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 275.39104599998154 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_ctc_metrics[3d]",
            "value": 0.24190016960651284,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 4.133936746000018 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[2d]",
            "value": 0.6340515808772549,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 1.5771587520000026 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_matcher[3d]",
            "value": 0.055151461106425825,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 18.131885899999986 sec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[2d]",
            "value": 13.276825746761036,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 75.31920799999625 msec\nrounds: 1"
          },
          {
            "name": "tests/bench.py::test_iou_div_metrics[3d]",
            "value": 1.3497310739793835,
            "unit": "iter/sec",
            "range": "stddev: 0",
            "extra": "mean: 740.888329000029 msec\nrounds: 1"
          }
        ]
      }
    ]
  }
}