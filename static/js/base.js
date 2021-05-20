function setThemeOnCookie() {
    const section = document.querySelector("#sdl");
    section.className = lightThemeSelect() ? "sec dark" : "sec"
}

function onClickStatementToggle() {
    document.querySelector("#dl").onclick=lightThemeSelect();
}

function lightThemeSelect() {
    return document.cookie.match(/theme=sec dark/i) != null;
}

function toggleLightDark() {
    const section = document.querySelector("#sdl");
    const currentState = section.className;
    const newClass = section.className == "sec dark" ? "sec" : "sec dark";
    section.className = newClass;

    const endDate = new Date();
    endDate.setFullYear(endDate.getFullYear() + 10);


    document.cookie = "theme=" + (newClass == "sec" ? "sec" : "sec dark") + "; Expires=" + endDate + "; domain=127.0.0.1; path=/;"

}

(function() {
    setThemeOnCookie();
    onClickStatementToggle();
    document.querySelector("#dl").onclick=toggleLightDark
})();