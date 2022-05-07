from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/index')
@app.route('/sample_page')
@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!DOCTYPE html>
<html style="font-size: 16px;">
  <head>
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta charset="utf-8">
    <meta name="keywords" content="">
    <meta name="description" content="">
    <meta name="page_type" content="np-template-header-footer-from-plugin">
    <title>123</title>
    <link rel="stylesheet" href="{url_for('static', filename='nicepage.css')}" media="screen">
<link rel="stylesheet" href="{url_for('static', filename='123.css')}" media="screen">
    <script class="u-script" type="text/javascript" src="{url_for('static', filename='jquery.js')}" defer=""></script>
    <script class="u-script" type="text/javascript" src="{url_for('static', filename='nicepage.js')}" defer=""></script>
    <meta name="generator" content="Nicepage 4.9.5, nicepage.com">
    <link id="u-theme-google-font" rel="stylesheet" href="https://fonts.googleapis.com/css?family=Roboto:100,100i,300,300i,400,400i,500,500i,700,700i,900,900i|Open+Sans:300,300i,400,400i,500,500i,600,600i,700,700i,800,800i">
    
    
    <script type="application/ld+json">
		"@context": "http://schema.org",
		"@type": "Organization",
		"name": "",
		"logo": "{url_for('static', filename='images/default-logo.png')}"
</script>
    <meta name="theme-color" content="#478ac9">
    <meta property="og:title" content="123">
    <meta property="og:type" content="website">
  </head>
  <body class="u-body u-xl-mode">
    <section class="u-clearfix u-image u-section-1" id="sec-3b0c" data-image-width="1280" data-image-height="719">
      <div class="u-clearfix u-gutter-0 u-layout-wrap u-layout-wrap-1">
        <div class="u-layout">
          <div class="u-layout-row">
            <div class="u-container-style u-layout-cell u-size-22 u-layout-cell-1">
              <div class="u-container-layout u-container-layout-1">
                <div class="u-accordion u-accordion-1">
                  <div class="u-accordion-item">
                    <a class="active u-accordion-link u-button-style u-text-palette-3-light-1 u-accordion-link-1" id="link-c55d" aria-controls="c55d" aria-selected="true">
                      <span class="u-accordion-link-text">Жанр</span>
                    </a>
                    <div class="u-accordion-active u-accordion-pane u-container-style u-accordion-pane-1" id="c55d" aria-labelledby="link-c55d">
                      <div class="u-container-layout u-container-layout-2">
                        <a href="https://nicepage.com/k/clothing-store-website-templates" class="u-border-none u-btn u-button-style u-palette-4-base u-btn-1">Яой</a>
                        <a href="https://nicepage.com/k/clothing-store-website-templates" class="u-border-none u-btn u-button-style u-palette-4-base u-btn-2">Романтика</a>
                        <a href="https://nicepage.review" class="u-border-none u-btn u-button-style u-palette-4-base u-btn-3">Приключения</a>
                        <a href="https://nicepage.com/c/pets-animals-html-templates" class="u-border-none u-btn u-button-style u-palette-4-base u-btn-4">Семейное</a>
                      </div>
                    </div>
                  </div>
                  <div class="u-accordion-item">
                    <a class="u-accordion-link u-button-style u-text-palette-3-light-1 u-accordion-link-2" id="link-bb58" aria-controls="bb58" aria-selected="false">
                      <span class="u-accordion-link-text">Сценаристы</span>
                    </a>
                    <div class="u-accordion-pane u-container-style u-accordion-pane-2" id="bb58" aria-labelledby="link-bb58">
                      <div class="u-container-layout u-container-layout-3">
                        <a href="https://nicepage.com/website-builder" class="u-border-none u-btn u-button-style u-palette-4-base u-btn-5">Макото Синкай</a>
                        <a href="https://nicepage.com/k/ticket-html-templates" class="u-border-none u-btn u-button-style u-palette-4-base u-btn-6">Хаяо Миядзаки</a>
                        <a href="https://nicepage.com/k/test-website-templates" class="u-border-none u-btn u-button-style u-palette-4-base u-btn-7">Такэси Сюдо</a>
                      </div>
                    </div>
                  </div>
                  <div class="u-accordion-item">
                    <a class="u-accordion-link u-button-style u-text-palette-3-light-1 u-accordion-link-3" id="link-9d62" aria-controls="9d62" aria-selected="false">
                      <span class="u-accordion-link-text">Количество серий</span><span class="u-accordion-link-icon u-accordion-link-icon-hidden u-icon u-text-grey-40 u-icon-1"><svg class="u-svg-link" preserveAspectRatio="xMidYMin slice" viewBox="0 0 16 16" style=""><use xmlns:xlink="http://www.w3.org/1999/xlink" xlink:href="#svg-124d"></use></svg><svg class="u-svg-content" viewBox="0 0 16 16" x="0px" y="0px" id="svg-124d"><path d="M8,10.7L1.6,5.3c-0.4-0.4-1-0.4-1.3,0c-0.4,0.4-0.4,0.9,0,1.3l7.2,6.1c0.1,0.1,0.4,0.2,0.6,0.2s0.4-0.1,0.6-0.2l7.1-6
	c0.4-0.4,0.4-0.9,0-1.3c-0.4-0.4-1-0.4-1.3,0L8,10.7z"></path></svg></span>
                    </a>
                    <div class="u-accordion-pane u-container-style u-accordion-pane-3" id="9d62" aria-labelledby="link-9d62">
                      <div class="u-container-layout u-container-layout-4">
                        <a href="https://nicepage.com/k/arabic-style-html-templates" class="u-border-none u-btn u-button-style u-palette-4-base u-btn-8">Фильм</a>
                        <a href="https://nicepage.com/wordpress-themes" class="u-border-none u-btn u-button-style u-palette-4-base u-btn-9">Сериал</a>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="u-container-style u-layout-cell u-size-38 u-layout-cell-2">
              <div class="u-container-layout u-container-layout-5">
                <div data-interval="5000" data-u-ride="carousel" class="u-carousel u-expanded-width u-slider u-slider-1" id="carousel-15d0">
                  <ol class="u-absolute-hcenter u-carousel-indicators u-carousel-indicators-1">
                    <li data-u-target="#carousel-15d0" class="u-active u-active-grey-10 u-grey-30" data-u-slide-to="0"></li>
                    <li data-u-target="#carousel-15d0" class="u-active-grey-10 u-grey-30" data-u-slide-to="1"></li>
                  </ol>
                  <div class="u-carousel-inner" role="listbox">
                    <div class="u-active u-carousel-item u-container-style u-slide">
                      <div class="u-container-layout u-valign-bottom u-container-layout-6">
                        <div class="u-expanded-width u-gallery u-layout-grid u-lightbox u-no-transition u-show-text-none u-gallery-1">
                          <div class="u-gallery-inner u-gallery-inner-1">
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="#">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="853">
                                <img class="u-back-image u-expanded" src="images/1029ae0889ebe7a5be517e6f6ada71dc647ca268553ad12ea42137ea2969df59600565d31ed0f8194353913f595ebc15399a61dbb86e7ebc842055_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-1">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="#">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="853">
                                <img class="u-back-image u-expanded" src="images/9d45d7e51055117f1c6594fb5d025800563c73a6011d82590ef9f3749854b4bbef2d6c5efb7ce3bb79fdbe6788ab55fc3273414435e3948292942b_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-2">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="#">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="823">
                                <img class="u-back-image u-expanded" src="images/3b8bab6779c0895ab2b83b1c6b351e6060027ce81c4753587a539be9248484cb16c6e47db77bb93f93062a333106b1f251f7ef527a587e61181afc_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-3">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="#">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="853">
                                <img class="u-back-image u-expanded" src="images/518f72266cb6dc57a6d8bd9104b4dfba4e2d85fb9d76d5eb7a44e60ca31c20d35656ecd1df0780b945049b963e3af6cbfee2b21c0cd7b56388cbbd_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-4">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="#">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="854">
                                <img class="u-back-image u-expanded" src="images/60447c53a37b8d14e3f83bf18c8afc0d360e6b90b65f10e1031d6350ed3b527178cfa0a69d878c3626420469660c71338bf2c95fb88ee0ab0ea02d_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-5">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="#">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="852">
                                <img class="u-back-image u-expanded" src="images/4b311e07a2547fab5b46b51ac4f21322f3a5579274a14de257bb26acc41a0ba9da440a1c70374fe86489d5bb614a871696de943526b363b39a0489_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-6">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                    <div class="u-carousel-item u-container-style u-slide">
                      <div class="u-container-layout u-valign-bottom u-container-layout-7">
                        <div class="u-expanded-width u-gallery u-layout-grid u-lightbox u-no-transition u-show-text-none u-gallery-2">
                          <div class="u-gallery-inner u-gallery-inner-2">
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="blog/пост.html">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="853">
                                <img class="u-back-image u-expanded" src="images/02728caa3c76b524f233b78f30a7bee3c2389789a3756b7af3159202b839c66805f76c4d441a42788e1f99b2318afb6767ebb207427a56f1562ae8_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-7">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="blog/пост-1.html">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="853">
                                <img class="u-back-image u-expanded" src="images/788f00d1fc48329be87a175ddf901f5ec0c87f2969ebf064cb144e6a872aaf6bff1758b8e023e05b4f49558d9cf6542188d06f20a113c40dadd17a_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-8">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="blog/пост-2.html">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="853">
                                <img class="u-back-image u-expanded" src="images/2abe1d86d8b2ea1aa33b7307de2bb00bc87a30c77b1dd0adad1e7165dd8248f0e4fa8b6c35880455a1190cd800b7fc547dc564842fa957cd9ad68e_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-9">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="blog/пост-3.html">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="854">
                                <img class="u-back-image u-expanded" src="images/e2ad668a63b086857a8367563e41c1fc92a63ae82803398dc32ef1a14062afaeda684fadd4c68318c2c019ce81544d6079e3825ef47084707b3ed2_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-10">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="blog/пост-4.html">
                              <div class="u-back-slide" data-image-width="1280" data-image-height="854">
                                <img class="u-back-image u-expanded" src="images/242b453179c5a10d75db29d27f1fe5c78d88f396449c9f23ae43109eb0145bffedb21e8ebad5e252f53ecea03d8b1db6354404abe9eef7422f03f9_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-11">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                            <div class="u-effect-hover-zoom u-gallery-item" data-href="blog/пост-5.html">
                              <div class="u-back-slide" data-image-width="960" data-image-height="1280">
                                <img class="u-back-image u-expanded" src="images/05630ca1a262805b29e5d73fd2a08b48daa8b105e45ea6e7aba1acef3f6689d6cd8b3e80dd01377b97dc75994968d92e706c8071070cb4a3870764_1280.jpg">
                              </div>
                              <div class="u-over-slide u-shading u-over-slide-12">
                                <h3 class="u-gallery-heading"></h3>
                                <p class="u-gallery-text"></p>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                  <a class="u-absolute-vcenter u-carousel-control u-carousel-control-prev u-spacing-5 u-text-grey-30 u-carousel-control-1" href="#carousel-15d0" role="button" data-u-slide="prev">
                    <span aria-hidden="true">
                      <svg viewBox="0 0 477.175 477.175"><path d="M145.188,238.575l215.5-215.5c5.3-5.3,5.3-13.8,0-19.1s-13.8-5.3-19.1,0l-225.1,225.1c-5.3,5.3-5.3,13.8,0,19.1l225.1,225
                    c2.6,2.6,6.1,4,9.5,4s6.9-1.3,9.5-4c5.3-5.3,5.3-13.8,0-19.1L145.188,238.575z"></path></svg>
                    </span>
                    <span class="sr-only">Previous</span>
                  </a>
                  <a class="u-absolute-vcenter u-carousel-control u-carousel-control-next u-spacing-5 u-text-grey-30 u-carousel-control-2" href="#carousel-15d0" role="button" data-u-slide="next">
                    <span aria-hidden="true">
                      <svg viewBox="0 0 477.175 477.175"><path d="M360.731,229.075l-225.1-225.1c-5.3-5.3-13.8-5.3-19.1,0s-5.3,13.8,0,19.1l215.5,215.5l-215.5,215.5
                    c-5.3,5.3-5.3,13.8,0,19.1c2.6,2.6,6.1,4,9.5,4c3.4,0,6.9-1.3,9.5-4l225.1-225.1C365.931,242.875,365.931,234.275,360.731,229.075z"></path></svg>
                    </span>
                    <span class="sr-only">Next</span>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
    
    
    
    <section class="u-backlink u-clearfix u-grey-80">
      <a class="u-link" href="https://nicepage.com/html-templates" target="_blank">
        <span>HTML Template</span>
      </a>
      <p class="u-text">
        <span>created with</span>
      </p>
      <a class="u-link" href="https://nicepage.com/website-builder" target="_blank">
        <span>Best Website Builder</span>
      </a>. 
    </section>
  </body>
</html>
'''
    elif request.method == 'POST':
        print(request.form['email'])
        print(request.form['password'])
        print(request.form['class'])
        print(request.form['file'])
        print(request.form['about'])
        print(request.form['accept'])
        print(request.form['sex'])
        return "Форма отправлена"


if __name__ == '__main__':
    app.run(debug=True)