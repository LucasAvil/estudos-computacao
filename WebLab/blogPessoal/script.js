const botao = document.getElementById('botao-tema');

const temaSalvo = localStorage.getItem('preferencia-tema')

if (temaSalvo === 'dark') {
    document.body.classList.add('dark-mode')
}

botao.addEventListener('click', () => {
    document.body.classList.toggle('dark-mode');
    
    if (document.body.classList.contains('dark-mode')){
        localStorage.setItem('preferencia-tema', 'dark')
    } else {
        localStorage.setItem('preferencia-tema', 'light')
    }
});

const form = document.getElementById('formulario-contato');

if (form) {
    form.addEventListener('submit', function(evento) {
        const nome = document.getElementById('nome').value.trim();
        const email = document.getElementById('email').value.trim();

        if (nome === "" || !email.includes("@")) {
            evento.preventDefault();
            alert("Preencha com um nome e um email válido.");
        }
    });
}

const btnAumentar = document.getElementById('btn-aumentar');
const btnDiminuir = document.getElementById('btn-diminuir');

let tamanhoAtual = 100;

if (btnAumentar) {
    btnAumentar.addEventListener('click', () => {
        if (tamanhoAtual < 140) {
            tamanhoAtual += 10;
            document.body.style.fontSize = tamanhoAtual + '%';
        }
    });
}

if (btnDiminuir) {
    btnDiminuir.addEventListener('click', () => {
        if (tamanhoAtual > 80) {
            tamanhoAtual -= 10;
            document.body.style.fontSize = tamanhoAtual + '%';
        }
    });
}