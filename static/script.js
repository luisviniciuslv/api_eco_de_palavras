window.onload = () => {
  let form = document.getElementById('form');

  console.log(form)

  form.addEventListener('submit', function(event) {
    event.preventDefault();

    let author = document.getElementById('author').value
    let message = document.getElementById('message').value

    let data = {
      author,
      message
    }

    fetch('/', {
      method: 'POST',
      body: JSON.stringify(data),
      headers: {
        'Content-Type': 'application/json'
      }
    }).then((response) => {
      if (response.status === 201) {
        alert('Postado com sucesso')
      } 
      if (response.status === 429) {
        alert('O limite é de 1 post a cada 5 minutos, aguarde')
      }
    })
    window.location.href = '/'
  })
}