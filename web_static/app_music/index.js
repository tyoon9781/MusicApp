let w_init = window.innerWidth
let h_init = window.innerHeight
let screen_info_str = `current screen : (${w_init}, ${h_init})`
document.getElementById('currentScreenInfo').innerHTML = screen_info_str

window.addEventListener("resize", () => {
    let w = window.innerWidth
    let h = window.innerHeight
    let screen_info_str = `current screen : (${w}, ${h})`
    document.getElementById('currentScreenInfo').innerHTML = screen_info_str
});
