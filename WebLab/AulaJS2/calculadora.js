const num1 = document.getElementById('num-1');
const num2 = document.getElementById('num-2');

const resultado = document.getElementById('resultado');

const btnSoma = document.getElementById('btn-soma');
const btnSub = document.getElementById('btn-sub');
const btnMult = document.getElementById('btn-mult');
const btnDiv = document.getElementById('btn-div');

function calcular(operador) {
  const a = Number(num1.value);
  const b = Number(num2.value);

  let resposta;
  if (operacao === 'soma') {
    resposta = a + b;
  }

  resultado.textContent = resposta;
}

btnSoma.addEventListener('click', () => {
  calcular('soma');
});
