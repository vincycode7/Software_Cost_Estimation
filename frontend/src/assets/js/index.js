const dataType = [
  {
    id: "id0",
    name: "MaxWell",
    listInner: {
      list: [
        {
          name: "Preprocessing Result",
          path: "../../backend/precrossing_data_ouput/maxwell/dataset/maxwell_raw.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../../backend/precrossing_data_ouput/maxwell/dataset/maxwell_raw.csv",
              header: false,
            },
            {
              name: "Feature To Category",
              path: "../../backend/precrossing_data_ouput/maxwell/dataset/convert_to_cat_features.csv",
              header: false,
            },
            {
              name: "Replace Missing With 'Nan'",
              path: "../../backend/precrossing_data_ouput/maxwell/dataset/fill_out_missing_for_cat2.csv",
              header: false,
            },
            {
              name: "Replace 'Nan' With Values (MICE)",
              path: "../../backend/precrossing_data_ouput/maxwell/dataset/after_mice_imputer.csv",
              header: false,
            },
            {
              name: "Round Off",
              path: "../../backend/precrossing_data_ouput/maxwell/dataset/after_round_of_values.csv",
              header: true,
            },
            {
              name: "One Hot Encoded Data",
              path: "../../backend/precrossing_data_ouput/maxwell/dataset/after_one_hot_encoding.csv",
              header: false,
            },
            {
              name: "Scaled Data",
              path: "../../backend/precrossing_data_ouput/maxwell/dataset/maxwell_standardization.csv",
              header: true,
            }
          ],
        },
        {
          name: "Maxwell With Kmeans",
          path: "../../backend/dataset/with_kmeans_1maxwell_x_before_split.csv",
          header: true,
          buttons: [
            {
              name: "X Before Split",
              path: "../../backend/dataset/with_kmeans_1maxwell_x_before_split.csv",
              header: false,
            },
            {
              name: "y Before Split",
              path: "../../backend/dataset/with_kmeans_1maxwell_y_before_split.csv",
              header: false,
            },
            {
              name: "X KNN Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_1maxwell_x1_after_split.csv",
              header: false,
            },
            {
              name: "y KNN Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_1maxwell_y1_after_split.csv",
              header: false,
            },
            {
              name: "X Lasso Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_1maxwell_x2_after_split.csv",
              header: false,
            },
            {
              name: "y Lasso Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_1maxwell_y2_after_split.csv",
              header: false,
            },


            {
              name: "X Learner 1 Output",
              path: "../../backend/dataset/with_kmeans_1maxwell_xlevel_0learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "y Learner 1 Output",
              path: "../../backend/dataset/with_kmeans_1maxwell_ylevel_0learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "X Learner 2 Output",
              path: "../../backend/dataset/with_kmeans_1maxwell_xlevel_1learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "y Learner 2 Output",
              path: "../../backend/dataset/with_kmeans_1maxwell_ylevel_1learneralgorithm1_during_training.csv",
              header: false,
            },
            
          ],
        },
        {
          name: "Maxwell Without Kmeans",
          path: "../../backend/dataset/with_kmeans_0maxwell_x_before_split.csv",
          header: true,
          buttons: [
            {
              name: "X Before Split",
              path: "../../backend/dataset/with_kmeans_0maxwell_x_before_split.csv",
              header: false,
            },
            {
              name: "y Before Split",
              path: "../../backend/dataset/with_kmeans_0maxwell_y_before_split.csv",
              header: false,
            },
            {
              name: "X KNN Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_0maxwell_x1_after_split.csv",
              header: false,
            },
            {
              name: "y KNN Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_0maxwell_y1_after_split.csv",
              header: false,
            },
            {
              name: "X Lasso Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_0maxwell_x1_after_split.csv",
              header: false,
            },
            {
              name: "y Lasso Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_0maxwell_y1_after_split.csv",
              header: false,
            },


            {
              name: "X Learner 1 Output",
              path: "../../backend/dataset/with_kmeans_0maxwell_xlevel_0learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "y Learner 1 Output",
              path: "../../backend/dataset/with_kmeans_0maxwell_ylevel_0learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "X Learner 2 Output",
              path: "../../backend/dataset/with_kmeans_0maxwell_xlevel_1learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "y Learner 2 Output",
              path: "../../backend/dataset/with_kmeans_0maxwell_ylevel_1learneralgorithm1_during_training.csv",
              header: false,
            },
            
          ],
        }
      ],
    },
  },
  {
    id: "id1",
    name: "Desh",
    listInner: {
      list: [
        {
          name: "Preprocessing Result",
          path: "../../backend/precrossing_data_ouput/desh/dataset/desh_raw.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../../backend/precrossing_data_ouput/desh/dataset/desh_raw.csv",
              header: false,
            },
            {
              name: "Replace Missing With 'Nan'",
              path: "../../backend/precrossing_data_ouput/desh/dataset/fill_missing_with_nan.csv",
              header: false,
            },
            {
              name: "Replace 'Nan' With Values (MICE)",
              path: "../../backend/precrossing_data_ouput/desh/dataset/fill_nan_with_mice_imputer.csv",
              header: false,
            },
            {
              name: "Round Off",
              path: "../../backend/precrossing_data_ouput/desh/dataset/after_round_off_value.csv",
              header: true,
            },
            {
              name: "Scaled Data",
              path: "../../backend/precrossing_data_ouput/desh/dataset/desh_standardizatino.csv",
              header: true,
            }
            
          ],
        },
        {
          name: "Desh With Kmeans",
          path: "../../backend/dataset/with_kmeans_1desh_x_before_split.csv",
          header: true,
          buttons: [
            {
              name: "X Before Split",
              path: "../../backend/dataset/with_kmeans_1desh_x_before_split.csv",
              header: false,
            },
            {
              name: "y Before Split",
              path: "../../backend/dataset/with_kmeans_1desh_y_before_split.csv",
              header: false,
            },
            {
              name: "X KNN Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_1desh_x1_after_split.csv",
              header: false,
            },
            {
              name: "y KNN Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_1desh_y1_after_split.csv",
              header: false,
            },
            {
              name: "X Lasso Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_1desh_x2_after_split.csv",
              header: false,
            },
            {
              name: "y Lasso Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_1desh_y2_after_split.csv",
              header: false,
            },


            {
              name: "X Learner 1 Output",
              path: "../../backend/dataset/with_kmeans_1desh_xlevel_0learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "y Learner 1 Output",
              path: "../../backend/dataset/with_kmeans_1desh_ylevel_0learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "X Learner 2 Output",
              path: "../../backend/dataset/with_kmeans_1desh_xlevel_1learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "y Learner 2 Output",
              path: "../../backend/dataset/with_kmeans_1desh_ylevel_1learneralgorithm1_during_training.csv",
              header: false,
            },
            
          ]
        },
        {
          name: "Desh Without Kmeans",
          path: "../../backend/dataset/with_kmeans_0desh_x_before_split.csv",
          header: true,
          buttons: [
            {
              name: "X Before Split",
              path: "../../backend/dataset/with_kmeans_0desh_x_before_split.csv",
              header: false,
            },
            {
              name: "y Before Split",
              path: "../../backend/dataset/with_kmeans_0desh_y_before_split.csv",
              header: false,
            },
            {
              name: "X KNN Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_0desh_x1_after_split.csv",
              header: false,
            },
            {
              name: "y KNN Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_0desh_y1_after_split.csv",
              header: false,
            },
            {
              name: "X Lasso Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_0desh_x1_after_split.csv",
              header: false,
            },
            {
              name: "y Lasso Learner 1 Input",
              path: "../../backend/dataset/with_kmeans_0desh_y1_after_split.csv",
              header: false,
            },


            {
              name: "X Learner 1 Output",
              path: "../../backend/dataset/with_kmeans_0desh_xlevel_0learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "y Learner 1 Output",
              path: "../../backend/dataset/with_kmeans_0desh_ylevel_0learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "X Learner 2 Output",
              path: "../../backend/dataset/with_kmeans_0desh_xlevel_1learneralgorithm1_during_training.csv",
              header: false,
            },
            {
              name: "y Learner 2 Output",
              path: "../../backend/dataset/with_kmeans_0desh_ylevel_1learneralgorithm1_during_training.csv",
              header: false,
            },
            
          ]
        }
      ],
    },
  }
];

class WorkData {
  constructor() {}

  isTableShowing = false;

  // Functions
  createTable(array) {
    let headcontent = "",
      bodycontent = "";

    array.forEach(function (row, index) {
      if (index === 0) {
        headcontent += "<tr>";
        row.forEach(function (cell) {
          headcontent +=
            "<th class='p-4 text-left font-bold'>" + cell + "</th>";
        });
        headcontent += "</tr>";
      } else {
        bodycontent += "<tr>";
        row.forEach(function (cell) {
          bodycontent += "<td class='p-8'>" + cell + "</td>";
        });
        bodycontent += "</tr>";
      }
    });

    document.getElementById("thead").innerHTML = headcontent;
    document.getElementById("tbody").innerHTML = bodycontent;
  }
  async fetchData(path) {
    this.isTableShowing = true;

    this.checkTableShowing();
    let all, init;

    const response = await fetch(path);
    const realData = await response.text();
    all = realData.split("\n");
    if (init !== all.length) {
      init = all.length;
      var arr = [];
      all.forEach((el) => {
        let regex = /[;,]+/
        el = el.split(regex);
        arr.push(el);
      });

      this.createTable(arr);
    }
  }

  checkTableShowing = () => {
    if (data.isTableShowing === false) {
      document.getElementById("tableShowing").classList.add("hidden");
      document.getElementById("tableNotShowing").classList.remove("hidden");
    } else {
      document.getElementById("tableNotShowing").classList.add("hidden");
      document.getElementById("tableShowing").classList.remove("hidden");
    }
  };

}

let data = new WorkData("data");
