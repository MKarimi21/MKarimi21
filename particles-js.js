// Output Welcome message
output('Original console design by Matt Cowley https://codepen.io/MattCowley/pen/jqBbdG/')
output('')
output('Welcome to example console program.')

// User Commands
function echo (...a) {
  return a.join(' ')
}
echo.usage = "echo arg [arg ...]"
echo.doc = "Echos to output whatever arguments are input"

var cmds = {
  echo,
  clear,
  help
}

/*
 * * * * * * * * USER INTERFACE * * * * * * *
 */

function clear () {
  $("#outputs").html("")
}
clear.usage = "clear"
clear.doc = "Clears the terminal screen"

function help (cmd) {
  if (cmd) {
    let result = ""
    let usage = cmds[cmd].usage
    let doc = cmds[cmd].doc
    result += (typeof usage === 'function') ? usage() : usage
    result += "\n"
    result += (typeof doc === 'function') ? doc() : doc
    return result
  } else {
    let result = "**Commands:**\n\n"
    print = Object.keys(cmds)
    for (let p of print) {
      result += "- " + p + "\n"
    }
    return result
  }
}
help.usage = () => "help [command]"
help.doc = () => "Without an argument, lists available commands. If used with an argument displays the usage & docs for the command."

// Set Focus to Input
$('.console').click(function() {
  $('.console-input').focus()
})

// Display input to Console
function input() {
  var cmd = $('.console-input').val()
  $("#outputs").append("<div class='output-cmd'>" + cmd + "</div>")
  $('.console-input').val("")
  autosize.update($('textarea'))
  $("html, body").animate({
    scrollTop: $(document).height()
  }, 300);
  return cmd
}

// Output to Console
function output(print) {
  if (!window.md) {
    window.md = window.markdownit({
      linkify: true,
      breaks: true
    })
  }
  $("#outputs").append(window.md.render(print))  
  $(".console").scrollTop($('.console-inner').height());
}

// Break Value
var newLine = "<br/> &nbsp;";

autosize($('textarea'))

var cmdHistory = []
var cursor = -1

// Get User Command
$('.console-input').on('keydown', function(event) {
  if (event.which === 38) {
    // Up Arrow
    cursor = Math.min(++cursor, cmdHistory.length - 1)
    $('.console-input').val(cmdHistory[cursor])
  } else if (event.which === 40) {
    // Down Arrow
    cursor = Math.max(--cursor, -1)
    if (cursor === -1) {
      $('.console-input').val('')
    } else {
      $('.console-input').val(cmdHistory[cursor])
    }
  } else if (event.which === 13) {
    event.preventDefault();
    cursor = -1
    let text = input()
    let args = getTokens(text)[0]
    let cmd = args.shift().value
    args = args.filter(x => x.type !== 'whitespace').map(x => x.value)
    cmdHistory.unshift(text)
    if (typeof cmds[cmd] === 'function') {
      let result = cmds[cmd](...args)
      if (result === void(0)) {
        // output nothing
      } else if (result instanceof Promise) {
        result.then(output)
      } else {
        console.log(result)
        output(result)
      }
    } else if (cmd.trim() === '') {
      output('')
    } else {
      output("Command not found: `" + cmd + "`")
      output("Use 'help' for list of commands.")
    }
  }
});

//ParticlesBG
particlesJS('particles-js',{'particles':{'number':{'value':50},'color':{'value':'#ffffff'},'shape':{'type':'triangle','polygon':{'nb_sides':5}},'opacity':{'value':0.06,'random':false},'size':{'value':11,'random':true},'line_linked':{'enable':true,'distance':150,'color':'#ffffff','opacity':0.4,'width':1},'move':{'enable':true,'speed':4,'direction':'none','random':false,'straight':false,'out_mode':'out','bounce':false}},'interactivity':{'detect_on':'canvas','events':{'onhover':{'enable':false},'onclick':{'enable':true,'mode':'push'},'resize':true},'modes':{'push':{'particles_nb':4}}},'retina_detect':true},function(){});