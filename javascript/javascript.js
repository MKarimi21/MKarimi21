$(document).ready (()=> {
    window.setInterval(function (){
      console.log('log ...')
      if  ($('.squre').is(':visible')) {
        $('.squre').hide()
      }
      else {
        $('.squre').show()
      }
    }, 500)

    $('.aboutBody').hide()
    $('.expBody').hide()
    $('.eduBody').hide()
    $('.skillBody').hide()
    $('.licBody').hide()
    $('.pubBody').hide()
    $('.conBody').hide()

    $("#about").click(function (){
      console.log('s')
      $('.bgImg').fadeOut("slow")
      $('.mainBody').fadeOut("slow")
      setTimeout(function(){
        $('.aboutBody').fadeIn("slow")
      },1000)
    })

    $("#experience").click(function (){
      $('.bgImg').fadeOut("slow")
      $('.mainBody').fadeOut("slow")
      setTimeout(function(){
        $('.expBody').fadeIn("slow")
      },1000)
    })

    $("#education").click(function (){
      $('.bgImg').fadeOut("slow")
      $('.mainBody').fadeOut("slow")
      setTimeout(function(){
        $('.eduBody').fadeIn("slow")
      },1000)
    })

    $("#skill").click(function (){
      $('.bgImg').fadeOut("slow")
      $('.mainBody').fadeOut("slow")
      setTimeout(function(){
        $('.skillBody').fadeIn("slow")
      },1000)
    })

    $("#license").click(function (){
      $('.bgImg').fadeOut("slow")
      $('.mainBody').fadeOut("slow")
      setTimeout(function(){
        $('.licBody').fadeIn("slow")
      },1000)
    })

    $("#publications").click(function (){
      $('.bgImg').fadeOut("slow")
      $('.mainBody').fadeOut("slow")
      setTimeout(function(){
        $('.pubBody').fadeIn("slow")
      },1000)
    })

    $("#contact").click(function (){
      $('.bgImg').fadeOut("slow")
      $('.mainBody').fadeOut("slow")
      setTimeout(function(){
        $('.conBody').fadeIn("slow")
      },1000)
    })

    // back btn about body
    $('#backAbout').click(function(){
      $('.aboutBody').fadeOut("slow")
      setTimeout(function(){
        $('.mainBody').fadeIn("slow")
        $('.bgImg').fadeIn("slow")
      },1000)
    })
    // back btn exp body
    $('#backExp').click(function(){
      $('.expBody').fadeOut("slow")
      setTimeout(function(){
        $('.mainBody').fadeIn("slow")
        $('.bgImg').fadeIn("slow")
      },1000)
    })
    // back btn exp body
    $('#backEdu').click(function(){
      $('.eduBody').fadeOut("slow")
      setTimeout(function(){
        $('.mainBody').fadeIn("slow")
        $('.bgImg').fadeIn("slow")
      },1000)
    })
    // back btn skill body
    $('#backSkill').click(function(){
      $('.skillBody').fadeOut("slow")
      setTimeout(function(){
        $('.mainBody').fadeIn("slow")
        $('.bgImg').fadeIn("slow")
      },1000)
    })
    // back btn license body
    $('#backLicense').click(function(){
      $('.licBody').fadeOut("slow")
      setTimeout(function(){
        $('.mainBody').fadeIn("slow")
        $('.bgImg').fadeIn("slow")
      },1000)
    })
    // back btn Publications body
    $('#backPublications').click(function(){
      $('.pubBody').fadeOut("slow")
      setTimeout(function(){
        $('.mainBody').fadeIn("slow")
        $('.bgImg').fadeIn("slow")
      },1000)
    })
    // back btn license body
    $('#backContact').click(function(){
      $('.conBody').fadeOut("slow")
      setTimeout(function(){
        $('.mainBody').fadeIn("slow")
        $('.bgImg').fadeIn("slow")
      },1000)
    })
    // tooltips
    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    })
    $("body").tooltip({ selector: '[data-toggle=tooltip]' });

  })
