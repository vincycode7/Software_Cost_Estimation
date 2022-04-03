const dataType = [
  {
    id: "id0",
    name: "MaxWell",
    listInner: {
      list: [
        {
          name: "MaxWell",
          path: "../details/csv_files/access-code.csv",
          header: true,
          buttons: [
            {
              name: "MaxWell",
              path: "../details/csv_files/email.csv",
              header: false,
            },
            {
              name: "MaxWell",
              path: "../details/csv_files/email.csv",
              header: false,
            },
            {
              name: "MaxWell",
              path: "../details/csv_files/email.csv",
              header: true,
            },
          ],
        },
        {
          name: "MaxWell",
          path: "../details/csv_files/email.csv",
          header: true,
          buttons: []
        },
        {
          name: "MaxWell",
          path: "../details/csv_files/email.csv",
          header: false,
          buttons:[]
        },
      ],
    },
  },
  {
    id: "id1",
    name: "Maxwell Training With Kmean",
    listInner: {
      list: [
        {
          name: "MaxWell",
          path: "../details/csv_files/email.csv",
          header: true,
          buttons: [
            {
              name: "MaxWell",
              header: false,
              path: "../details/csv_files/email.csv",
            },
            {
              name: "MaxWell",
              path: "../details/csv_files/email.csv",
              header: false,
            },
            {
              name: "MaxWell",
              path: "../details/csv_files/email.csv",
              header: true,
            },
          ],
        },
        {
          name: "MaxWell",
          path: "../details/csv_files/email.csv",
          header: true,
          buttons: []
        },
        {
          name: "MaxWell",
          path: "../details/csv_files/email.csv",
          header: true,
          buttons: []
        },
      ],
    },
  },
  {
    id: "id2",
    name: "Maxwell Testing With Kmean",
    listInner: {
      list: [
        {
          name: "MaxWell",
          path: "../details/csv_files/email.csv",
          buttons: [
            {
              name: "MaxWell",
              path: "../details/csv_files/email.csv",
              header: true,
            },
            {
              name: "MaxWell",
              path: "../details/csv_files/access-code.csv",
              header: false,
            },
            {
              name: "MaxWell",
              header: true,
              path: "../details/csv_files/email.csv",
            },
          ],
        },
        {
          name: "MaxWell",
          header: false,
          path: "../details/csv_files/email.csv",
          buttons: []
        },
        {
          name: "MaxWell",
          header: false,
          path: "../details/csv_files/email.csv",
          buttons: []
        },
      ],
    },
  },
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

  timeout;
  moveToNewPage = () => {
    this.timeout = setTimeout(() => {
      window.location.assign("./table.html");
    }, 5000);
  };

  timer = 6;
  jump;
  setTimer = () => {
    this.jump = setInterval(() => {
      if (this.timer > 0) {
        this.timer -= 1;
        let seconds = "seconds";
        if (this.timer === 1 || this.timer === 0) {
          seconds = "second";
        }
        document.getElementById("timer").innerText = `${this.timer} ${seconds}`;
      }
    }, 1000);
  };
  clearTimer = () => {
    clearInterval(this.jump);
    clearTimeout(this.timeout);
  };
}

let data = new WorkData("data");
