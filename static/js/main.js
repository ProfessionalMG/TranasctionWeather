const alertBox = document.getElementById('alert-box')
const form = document.getElementById('a-form')
const address = document.getElementById('id_address')
const csrf = document.getElementsByName('csrfmiddlewaretoken')
const url = '/home'

form.addEventListener('submit', ev => {
    e.preventDefault()
    const fd = new FormData()
    fd.append('csrfmiddlewaretoken', csrf[0].value)
    fd.append('address', address.value)

    $.ajax({
        type: 'POST',
        url: url,
        data: fd,
        cache: false,
        contentType: false,
        processData: false,
    })
})