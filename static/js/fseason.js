const navigation = document.querySelector(".navigation");
const btn = document.getElementById("btn")
const pattern = document.querySelector(".pattern");


const br = document.querySelector("#br");
const brp = document.querySelector("#brp");
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
brp.addEventListener("click", trade)
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
//    pattern.classList.toggle("active");


    $(".test li .title").click(function() {
        var currentele = $(this).html();
        $(".pattern li span").html(currentele);
        btn.value = currentele
    })
}

//onkeyup="document.getElementById('input2').value=this.value"


document.querySelector("#mysearch").onkeyup = function() {
    const test = document.querySelector("#mysearch")
    const clear = document.querySelector("#clean");
    const btn = document.querySelector("#btn")

    if(test.value.length >= 3) {
        clear.classList.add("clear");
        btn.disabled = false;
        btn.classList.remove("disabled");

    } else {
        clear.classList.remove("clear");
        btn.disabled = true;
        btn.classList.add("disabled");
    }

    clear.onclick = function() {
        test.value = ""
        clear.classList.remove("clear");
        btn.disabled = true;
        btn.classList.add("disabled");
    }
}

