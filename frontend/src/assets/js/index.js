const dataType = [
  {
    id: "id0",
    name: "MaxWell",
    listInner: {
      list: [
        {
          name: "MaxWell With Kmeans",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../details/csv_files/email.csv",
              header: false,
            }
          ],
        },
        {
          name: "MaxWell With Kmeans",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../details/csv_files/email.csv",
              header: false,
            }
          ],
        },
        {
          name: "MaxWell With Kmeans",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../details/csv_files/email.csv",
              header: false,
            }
          ],
        },
        {
          name: "MaxWell With Kmeans",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../details/csv_files/email.csv",
              header: false,
            }
          ],
        },
        {
          name: "MaxWell With Kmeans",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../details/csv_files/email.csv",
              header: false,
            }
          ],
        },
        {
          name: "MaxWell With Kmeans",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../details/csv_files/email.csv",
              header: false,
            }
          ],
        },
        {
          name: "MaxWell With Kmeans",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../details/csv_files/email.csv",
              header: false,
            }
          ],
        },
        {
          name: "MaxWell With Kmeans",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../details/csv_files/email.csv",
              header: false,
            }
          ],
        },
        {
          name: "MaxWell With Kmeans",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../details/csv_files/email.csv",
              header: false,
            }
          ],
        },
        {
          name: "MaxWell With Kmeans",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              path: "../details/csv_files/email.csv",
              header: false,
            }
          ],
        },
        {
          name: "MaxWell Without Kmeans",
          path: "../details/csv_files/email.csv",
          header: true,
          buttons: [{
            name: "Raw Data",
            path: "../details/csv_files/email.csv",
            header: false,
          }]
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
          name: "Desh With Kmeans",
          path: "../details/csv_files/email.csv",
          header: true,
          buttons: [
            {
              name: "Raw Data",
              header: false,
              path: "../details/csv_files/email.csv",
            }
            
          ],
        },
        {
          name: "Desh Without Kmeans",
          path: "../details/csv_files/email.csv",
          header: true,
          buttons: [{
            name: "Raw Data",
            header: false,
            path: "../details/csv_files/email.csv",
          }]
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
        el = el.split(";") || el.split(",");
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
