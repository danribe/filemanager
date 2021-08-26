if (localStorage.getItem('token') == null) {
    alert('Usuário deslogado')
    location = "login.html"
}

function sair() {
    location = "login.html"
    localStorage.clear()
}
