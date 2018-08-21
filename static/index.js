us=null;
document.addEventListener('DOMContentLoaded', () => {
  if(localStorage.getItem('us'))==null)
      {
        // if the user has not enterd the user name an alert message will pop up
        setInterval(count,100000);
      }

  document.querySelector('#form1').onsubmit = () => {
    us= document.querySelector('#usr').value;
    // now js will store the user name and user need not to enter the name again and agian
    localStorage.setItem('us',us);
    return false
  };
  // Connect to websocket
  var socket = io.connect(location.protocol + '//' + document.domain + ':' + location.port);

  // When connected, configure submit button buttons
  socket.on('connect', () => {
    document.querySelector('#form4').onsubmit = () => {
      msg = document.querySelector('#msg').value;
            socket.emit('submit message', {'msg': msg});
          };
        });
        // When a new message is sent, add to message container
        socket.on('announce message', data => {
          if( typeof msg.user_name !== 'undefined' ) {
          $( 'h1' ).remove()
            const li = document.createElement('li');
            li.innerHTML = `message recorded: us ${data.msg}`;
            document.querySelector('#mss').append(li);

      });

function count(){
    alert('please enter the username and submit')
}
