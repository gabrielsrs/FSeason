function setThemeOnCookie() {
    const section = document.querySelector("#s_black_light");
    section.className = lightThemeSelect() ? "sec dark" : "sec"
}

function onClickStatementToggle() {
    document.querySelector("#t_black_light").onclick=lightThemeSelect();
}

function lightThemeSelect() {
    return document.cookie.match(/theme=sec dark/i) != null;
}

function toggleLightDark() {
    const section = document.querySelector("#s_black_light");
    const currentState = section.className;
    const newClass = section.className == "sec dark" ? "sec" : "sec dark";
    section.className = newClass;

    const endDate = new Date();
    endDate.setFullYear(endDate.getFullYear() + 10);


    document.cookie = "theme=" + (newClass == "sec" ? "sec" : "sec dark") + "; Expires=" + endDate + "; domain=fseason.herokuapp.com; path=/;"

}

(function() {
    setThemeOnCookie();
    onClickStatementToggle();
    document.querySelector("#t_black_light").onclick=toggleLightDark
})();