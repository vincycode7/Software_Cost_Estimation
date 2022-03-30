// New data structure
// [{
//  [{
//      [{
// 
//      }]
//  }]
// }]
const dataType = [
  {
    name: "MaxWell",
    path: "../details/csv_files/email.csv",
  },
  {
    name: "Maxwell Training With Kmean",
    path: "../details/csv_files/access-code.csv",
  },
  {
    name: "Maxwell Testing With Kmean",
    path: "../details/csv_files/access-password.csv",
  },
  {
    name: "Maxwell Results With Kmean",
    path: "../details/csv_files/access-code.csv",
  },
  {
    name: "Maxwell Training Without Kmean",
    path: "../details/csv_files/access-code.csv",
  },
  {
    name: "Maxwell Testing Without Kmean",
    path: "../details/csv_files/access-password.csv",
  },
  {
    name: "Maxwell Results Without Kmean",
    path: "../details/csv_files/access-code.csv",
  },
  {
    name: "Desh",
    path: "../details/csv_files/email-password.csv",
  },
  {
    name: "Desh Training With Kmean",
    path: "../details/csv_files/access-code.csv",
  },
  {
    name: "Desh Testing With Kmean",
    path: "../details/csv_files/access-password.csv",
  },
  {
    name: "Desh Results With Kmean",
    path: "../details/csv_files/access-code.csv",
  },
  {
    name: "Desh Training Without Kmean",
    path: "../details/csv_files/access-code.csv",
  },
  {
    name: "Desh Testing Without Kmean",
    path: "../details/csv_files/access-password.csv",
  },
  {
    name: "Desh Results Without Kmean",
    path: "../details/csv_files/access-code.csv",
  },
  {
    name: "Results",
    path: "../details/csv_files/access-code.csv",
  },
  // {
  //   name: "drap mud",
  //   path: "../details/csv_files/access-code.csv",
  // },
  // {
  //   name: "master",
  //   path: "../details/csv_files/access-code.csv",
  // },
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
  async fetchData(e) {
    this.isTableShowing = true;

    this.checkTableShowing();
    let all, init;
    let path = dataType.find((item) => {
      return item.name.toLowerCase() === e.target.innerText.toLowerCase();
    });
    const response = await fetch(path.path);
    const realData = await response.text();
    all = realData.split("\n");
    if (init !== all.length) {
      init = all.length;
      var arr = [];
      all.forEach((el) => {
        el = el.split(";");
        arr.push(el);
      });

      this.createTable(arr);
    }
  }

  createSidebar = (id) => {
    let data = document.getElementById(id);
    dataType.forEach((project) => {
      return (data.innerHTML += `<button onclick="data.fetchData(event)" class='list-none h-16 slideDown focus:outline-none  font-medium capitalize text-gray-600 hover:bg-clifford-300 focus:bg-clifford focus:text-white hover:text-white transition-all duration-300 cursor-pointer'><span class='flex getborder hover:border-none  items-center h-full w-8/12 mx-auto'>${project.name}<span></button>`);
    });
  };

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
  clearTimer=()=>{
    clearInterval(this.jump);
    clearTimeout(this.timeout)
  }
}

let data = new WorkData("data");
