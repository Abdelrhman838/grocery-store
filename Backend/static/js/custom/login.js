const input1 = document.querySelector("#d1")
const input2 = document.querySelector("#d2")

function Elfocus1(){
    input1.classList.toggle("focus")
}
function Elfocus2(){
    input2.classList.toggle("focus")
}
function login(){
    const username = input1.value;
    localStorage.setItem("username",username)
}