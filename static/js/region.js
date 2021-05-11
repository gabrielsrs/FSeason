const navigation = document.querySelector(".navigation");

const br = document.querySelector("#br");
const eun = document.querySelector("#eun");
const euw = document.querySelector("#euw");
const jp = document.querySelector("#jp");
const kr = document.querySelector("#kr");
const las = document.querySelector("#las");
const lan = document.querySelector("#lan");
const na = document.querySelector("#na");
const oc = document.querySelector("#oc");
const ru = document.querySelector("#ru");
const tr = document.querySelector("#tr");

br.addEventListener("click", trade)
eun.addEventListener("click", trade)
euw.addEventListener("click", trade)
jp.addEventListener("click", trade)
kr.addEventListener("click", trade)
las.addEventListener("click", trade)
lan.addEventListener("click", trade)
na.addEventListener("click", trade)
oc.addEventListener("click", trade)
ru.addEventListener("click", trade)
tr.addEventListener("click", trade)

function trade() {
    navigation.classList.toggle("active");
}