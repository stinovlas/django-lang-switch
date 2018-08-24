const lang_switches = document.querySelectorAll('div.lang-switch')

function send_this_form() {
    this.form.submit()
}

lang_switches.forEach(function(lswitch) {
    const select = lswitch.querySelector('select')
    select.addEventListener('change', send_this_form)
})
