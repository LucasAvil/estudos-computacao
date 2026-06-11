const num1 = document.querySelector('#num1');
const num2 = document.querySelector('#num2');
const resultado = document.querySelector('#resultado');

const btnSoma = document.querySelector('#btn-soma');
const btnSubtracao = document.querySelector('#btn-subtracao');
const btnMultiplicacao = document.querySelector('#btn-multiplicacao');
const btnDivisao = document.querySelector('#btn-divisao');

function calcular(operacao) {
  // .value retorna o conteúdo de um <input> como TEXTO (string)
  // Number() converte esse texto para número
  const a = Number(num1.value);
  const b = Number(num2.value);

  // Variável que vai guardar o resultado antes de exibir
  let resposta;

  // Cada operação matemática básica:
  if (operacao === 'soma') {
    resposta = a + b;
  } else if (operacao === 'subtracao') {
    resposta = a - b;
  } else if (operacao === 'multiplicacao') {
    resposta = a * b;
  } else if (operacao === 'divisao') {
    // Boa prática: verificar divisão por zero antes de calcular
    if (b === 0) {
      resultado.textContent = 'Erro: divisão por zero!';
      return; // interrompe a função aqui
    }
    resposta = a / b;
  }

  // .textContent altera o texto visível do elemento no HTML
  resultado.textContent = resposta;
}

// Registrar os eventos de clique ──────
//
// addEventListener('click', função) diz ao navegador:
// "quando este botão for clicado, execute esta função"
//
// A arrow function ( () => {} ) é a função que será executada.
// Dentro dela, chamamos calcular() com o nome da operação.

btnSoma.addEventListener('click', () => {
  calcular('soma');
});

btnSubtracao.addEventListener('click', () => {
  calcular('subtracao');
});

btnMultiplicacao.addEventListener('click', () => {
  calcular('multiplicacao');
});

btnDivisao.addEventListener('click', () => {
  calcular('divisao');
});

//
// Desafio 1 — Botão Limpar
//   O botão "Limpar" já existe no HTML.
//   Faça-o apagar os dois inputs e resetar o resultado para "—".
//
// Desafio 2 — Validação de campos vazios
//   Antes de calcular, verifique se os dois campos foram preenchidos.
//   Se algum estiver vazio, exiba: "Preencha os dois campos!"
//   Dica: if (num1.value === '' || num2.value === '') { ... }
//
// Desafio 3 — Tecla Enter executa a soma
//   Ao pressionar Enter em qualquer lugar da página, execute a soma.
//   Dica: use o evento 'keydown' no document e verifique e.key === 'Enter'
//

// ════════════════════════════════════════════════════════════════════════════
// GABARITO
// ════════════════════════════════════════════════════════════════════════════

// ── Gabarito 1 — Botão Limpar ────────────────────────────────────────────
const btnLimpar = document.querySelector('#btn-limpar');

btnLimpar.addEventListener('click', () => {
  num1.value = ''; // apaga o primeiro input
  num2.value = ''; // apaga o segundo input
  resultado.textContent = '—'; // reseta o texto do resultado
  num1.focus(); // devolve o foco para o primeiro campo
});

// ── Gabarito 2 — Validação de campos vazios ──────────────────────────────
// Para aplicar, substitua a função calcular() original por esta:
//
// function calcular(operacao) {
//   if (num1.value === '' || num2.value === '') {
//     resultado.textContent = 'Preencha os dois campos!';
//     return;  // interrompe a função aqui, sem calcular nada
//   }
//   const a = Number(num1.value);
//   const b = Number(num2.value);
//   let resposta;
//   if (operacao === 'soma')               resposta = a + b;
//   else if (operacao === 'subtracao')     resposta = a - b;
//   else if (operacao === 'multiplicacao') resposta = a * b;
//   else if (operacao === 'divisao') {
//     if (b === 0) { resultado.textContent = 'Erro: divisão por zero!'; return; }
//     resposta = a / b;
//   }
//   resultado.textContent = resposta;
// }

// ── Gabarito 3 ampliado: Eventos de teclado ──────────────────────────────
document.addEventListener('keydown', (e) => {
  // e.key contém o nome da tecla pressionada como string
  if (e.key === '+') {
    calcular('soma');
  }
  if (e.key === '-') {
    calcular('subtracao');
  }
  if (e.key === '*') {
    calcular('multiplicacao');
  }
  if (e.key === '/') {
    calcular('divisao');
  }
  if (e.key === '.') {
    alert('Tecla sem operação');
  }
});

///// manipulacao de css com js

const btnDark = document.querySelector('#btn-dark');
btnDark.addEventListener('click', () => {
  document.body.classList.remove(
    'tema-roxo',
    'tema-verde',
    'tema-laranja',
    'alto-contraste',
  );
  document.body.classList.toggle('dark');
});

const btnAumentaFonte = document.querySelector('#btn-fonte-mais');
const btnDiminuiFonte = document.querySelector('#btn-fonte-menos');

btnAumentaFonte.addEventListener('click', () => {
  const tamanhoAtual = parseFloat(
    getComputedStyle(document.documentElement).fontSize,
  );
  if (tamanhoAtual < 35) {
    document.documentElement.style.fontSize = tamanhoAtual + 2 + 'px';
  }
});

btnDiminuiFonte.addEventListener('click', () => {
  const tamanhoAtual = parseFloat(
    getComputedStyle(document.documentElement).fontSize,
  );
  if (tamanhoAtual > 10) {
    document.documentElement.style.fontSize = tamanhoAtual - 2 + 'px';
  }
});

const btnContraste = document.querySelector('#btn-contraste');
btnContraste.addEventListener('click', () => {
  document.body.classList.remove(
    'dark',
    'tema-roxo',
    'tema-verde',
    'tema-laranja',
  );
  document.body.classList.toggle('alto-contraste');
});

const btnPadrao = document.querySelector('#btn-tema-padrao');
const btnRoxo = document.querySelector('#btn-tema-roxo');
const btnVerde = document.querySelector('#btn-tema-verde');
const btnLaranja = document.querySelector('#btn-tema-laranja');

btnPadrao.addEventListener('click', () => {
  document.body.classList.remove(
    'dark',
    'tema-roxo',
    'tema-verde',
    'tema-laranja',
    'alto-contraste',
  );
  document.body.classList.toggle(':root');
});

btnRoxo.addEventListener('click', () => {
  document.body.classList.remove(
    'dark',
    'tema-verde',
    'tema-laranja',
    'alto-contraste',
  );
  document.body.classList.toggle('tema-roxo');
});

btnVerde.addEventListener('click', () => {
  document.body.classList.remove(
    'dark',
    'tema-roxo',
    'alto-contraste',
    'tema-laranja',
  );
  document.body.classList.toggle('tema-verde');
});

btnLaranja.addEventListener('click', () => {
  document.body.classList.remove(
    'dark',
    'tema-roxo',
    'tema-verde',
    'alto-contraste',
  );
  document.body.classList.toggle('tema-laranja');
});
