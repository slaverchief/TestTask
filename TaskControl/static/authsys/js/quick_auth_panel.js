function login_click(){
    var login_container = document.getElementById('login_container')
    var signup_container = document.getElementById('signup_container')
    if (login_container.hidden == true){
        login_container.hidden = false
        if (signup_container.hidden == false){
            signup_container.hidden = true
        }
    }
    else{
        login_container.hidden = true
    }
}

function signup_click(){
    var login_container = document.getElementById('login_container')
    var signup_container = document.getElementById('signup_container')
    if (signup_container.hidden == true){
        signup_container.hidden = false
        if (login_container.hidden == false){
            login_container.hidden = true
        }
    }
    else{
        signup_container.hidden = true
    }
}