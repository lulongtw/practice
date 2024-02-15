let inputs = document.querySelectorAll("[type='text']");
let height = inputs[0];
let weight = inputs[1];
let bmiResult;
let data = [];
let recordWrap = document.querySelector(".recordWrap");
let re = document.querySelector(".REButton");
let resCir = document.querySelector(".showResultCircle");
let see = document.querySelector(".seeResultCircle");
let delAll = document.querySelector(".delAll");

for (item of inputs) {
  item.addEventListener("input", (e) => {
    let val = e.target.value;
    val = val.replace(/[^0-9]/g, "");
    e.target.value = val;
  });
}


window.onkeydown = (e) => {
  if (e.key == "Enter") {
    pushData();
  }
};

function pushData() {
  if (checked()) {
    let currentData = getBmiResult();
    data.push(currentData);
    saveToLocal(data);
    refreshMain(data);
    toggleResultCircle(currentData);
  } else {
    height.value = height.value ? height.value : "你他媽";
    weight.value = weight.value ? weight.value : "給我輸入";
  }
}

window.onload = () => {
  data = getFromLocal() ? getFromLocal() : [];
  refreshMain(data);
};

function checked() {
  return height.value && weight.value ? true : false;
}

function getBmiResult() {
  bmiResult = (
    parseInt(weight.value) /
    (parseInt(height.value) * 0.01) ** 2
  ).toFixed(2);
  return {
    height: height.value,
    weight: weight.value,
    bmi: bmiResult,
    time: getTime(),
    comment: getComment(bmiResult),
  };
}

function getTime() {
  let date = new Date();
  let day = date.getDate();
  let month = date.getMonth() + 1;
  let year = date.getFullYear();
  return {
    day: day,
    month: month,
    year: year,
  };
}

function getComment(bmi) {
  switch (true) {
    case bmi < 16:
      return ["排骨飯", "blue"];
    case bmi >= 16 && bmi < 25:
      return ["正常", "green"];
    case bmi >= 25 && bmi < 30:
      return ["有點肥", "orange"];
    case bmi > -30 && bmi < 35:
      return ["蠻肥的", "red"];
    default:
      return ["嚴重優秀", "brown"];
  }
}

function refreshMain(data) {
  recordWrap.innerHTML = "";
  let c = 0;
  for (item of data) {
    // console.log(item)
    recordWrap.innerHTML += `
    <div class="record" style="border-color:${item.comment[1]}">
    <div class="recordComment">${item.comment[0]}</div>
    <div class="recordBMI"><span>BMI</span><span>${item.bmi}</span></div>
    <div class="recordWeight"><span>weight</span><span>${item.weight}KG</span></div>
    <div class="recordTime">${item.time.day}-${item.time.month}-${item.time.year}</div>
    <div class="delButton" data-idx='${c}' onclick='del(event)'>X</div>
  </div>
    `;
    c++;
  }
}
function del(e) {
  data.splice(parseInt(e.target.dataset.idx), 1);
  saveToLocal(data);
  refreshMain(data);
}

function saveToLocal(data) {
  let toLocal = JSON.stringify(data);
  localStorage.setItem("fatman", toLocal);
}
function getFromLocal() {
  return JSON.parse(localStorage.getItem("fatman"));
}
function toggleResultCircle(currentData) {
  resCir.style.color = currentData.comment[1];
  resCir.style.borderColor = currentData.comment[1];
  re.style.backgroundColor = currentData.comment[1];
  resCir.style.borderColor = currentData.comment[1];
  let bmi = document.querySelector(".bmi");
  bmi.textContent = currentData.bmi;
  let cmnt = document.querySelector(".comment");
  cmnt.textContent = currentData.comment[0];
  resCir.style.display = "flex";

  see.style.display = "none";
}

re.onclick = () => {
  resCir.style.display = "none";
  see.style.display = "block";
};
see.onclick = () => {
  pushData();
};
delAll.onclick = () => {
  data = [];
  refreshMain(data);
  saveToLocal(data);
};
