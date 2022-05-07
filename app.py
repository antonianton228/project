from flask import Flask, render_template, request, url_for, redirect, jsonify, request
import sqlite3

bd = sqlite3.connect('dataB.db', check_same_thread=False)
cur = bd.cursor()

app = Flask(__name__)

cur.execute(f"""CREATE TABLE IF NOT EXISTS users(
   username TEXT,
   rate TEXT,
   mail TEXT,
   report TEXT);
""")
bd.commit()


@app.route('/')
@app.route('/index')
@app.route('/sample_page')
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return redirect(f'http://{request.environ.get("HTTP_X_REAL_IP", request.remote_addr)}:5000/static/123.html')
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


@app.route('/static/form.html')
@app.route('/static/form.html', methods=['post', 'get'])
def form():
    message = ''
    if request.method == 'POST':
        username = request.form.get('name')
        rate = request.form.get('text')
        email = request.form.get('email')
        mess = request.form.get('textarea')

        cur.executemany(f"INSERT INTO users VALUES(?, ?, ?, ?);", [(username, rate, email, mess)])
        bd.commit()

        print(username, rate, email, mess)
    return f'''
        <!DOCTYPE html>
<html style="font-size: 16px;">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>form</title>
    <link rel="stylesheet" href="nicepage.css" media="screen">
<link rel="stylesheet" href="form.css" media="screen">
    <script class="u-script" type="text/javascript" src="jquery.js" defer=""></script>
    <script class="u-script" type="text/javascript" src="nicepage.js" defer=""></script>
    <meta name="generator" content="Nicepage 4.9.5, nicepage.com">
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">
    
    
    <script type="application/ld+json">
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": ""
</script>
    <meta name="theme-color" content="#478ac9">
    <meta property="og:title" content="form">
    <meta property="og:type" content="website">
  </head>
  <body class="u-body u-xl-mode">
    <section class="u-clearfix u-image u-section-1" id="sec-7602" data-image-width="1280" data-image-height="800">
      <div class="u-clearfix u-sheet u-valign-middle u-sheet-1">
        <div class="u-container-style u-custom-color-1 u-group u-preserve-proportions u-radius-15 u-shape-round u-group-1">
          <div class="u-container-layout u-container-layout-1">
            <div class="u-form u-form-1">
              <form action="#" method="POST" class="u-clearfix u-form-spacing-10 u-form-vertical u-inner-form" source="email" name="form" style="padding: 10px;">
                
                
                <div class="u-form-group u-form-name">
                  <label for="name-bd66" class="u-label">Ваше имя</label>
                  <input type="text" placeholder="Введите Ваше имя" id="name-bd66" name="name" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" required="">
                </div>
                <div class="u-form-group u-form-group-2">
                  <label for="text-9a2b" class="u-label">Впечатлние о сайте (по шкале от 0 до 10, где 0 - очень плохо, все переделать, 10 - замечательно, прогламмистов похвалить): </label>
                  <input type="text" placeholder="0-10" id="text-9a2b" name="text" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white">
                </div>
                <div class="u-form-email u-form-group">
                  <label for="email-bd66" class="u-label">Эл. почта для получения обратной связи</label>
                  <input type="email" placeholder="Введите Ваш email адрес" id="email-bd66" name="email" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" required="">
                </div>
                <div class="u-form-group u-form-textarea u-form-group-4">
                  <label for="textarea-7fee" class="u-label">Пожелания и предложения (Можете написать про любимое Аниме)</label>
                  <textarea rows="4" cols="50" id="textarea-7fee" name="textarea" class="u-border-1 u-border-grey-30 u-input u-input-rectangle u-white" required=""></textarea>
                </div>
                <div class="u-align-left u-form-group u-form-submit">
                  <a href="#" class="u-btn u-btn-submit u-button-style">Отправить</a>
                  <input type="submit" value="submit" class="u-form-control-hidden">
                </div>
                <div class="u-form-send-message u-form-send-success"> Спасибо! Ваше сообщение отправлено. </div>
                <div class="u-form-send-message u-form-send-message"> Спасибо! Ваше сообщение отправлено. </div>
                <input type="hidden" value="" name="recaptchaResponse">
              </form>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    
    <footer class="u-align-center u-clearfix u-footer u-grey-80 u-footer" id="sec-6038"><div class="u-clearfix u-sheet u-sheet-1">
        <p class="u-small-text u-text u-text-variant u-text-1"> Сайт создан благодаря гениальным идеям Колгановой Виктории и помощи Сурниной Анастасии. <br>Для улучшения нашего продукта оставьте обратную связь:&nbsp;&nbsp;<br>Заранее благодарим за продвидение нашего сайта в массы<br>
          <br>
          <br>Контакты с программистами: +7&nbsp;968&nbsp;664 5501<br>&nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; &nbsp; +7&nbsp;903&nbsp;252 3693<br>
        </p>
        <a href="form.html" data-page-id="59325538" class="u-btn u-button-style u-btn-1">Помочь)</a>
      </div></footer>
    <section class="u-backlink u-clearfix u-grey-80">
      <a class="u-link" href="https://nicepage.com/website-templates" target="_blank">
        <span>Website Templates</span>
      </a>
      <p class="u-text">
        <span>created with</span>
      </p>
      <a class="u-link" href="" target="_blank">
        <span>Website Builder Software</span>
      </a>. 
    </section>
  </body>
</html>
'''


if __name__ == '__main__':
    app.run(debug=True)
#
# @app.route('/')
# def gotostart():
#