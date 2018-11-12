def create_html():
    create_form = "<form>\n"
    create_form = gen_options(create_form)
    create_form += gen_submit() + "\n"
    create_form += "</form>"
    return create_form


def gen_colors():
    colors = {
        '#ff9900': 'orange',
        '#00ff00': 'vert',
        '#ff0000': 'rouge',
        '#ff00ff': 'violet',
        '#0000ff': 'bleu',
        '#000000': 'noir',
        '#ffffff': 'blanc',
        '#ffff00': 'jaune'
    }
    return colors


def gen_options(message):
    message += "\t<select name='colors'>\n"
    colors = gen_colors()
    for keys, item in colors.items():
        message += "\t\t<option value=" + keys + ">" + item + "</option> \n"
    message += "\t</select>\n"
    return message


def gen_submit():
    return "\t<input type='submit' value='Envoyer'>"

