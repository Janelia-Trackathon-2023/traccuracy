window.BENCHMARK_DATA = {
  "lastUpdate": 1707155491821,
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
      }
    ]
  }
}