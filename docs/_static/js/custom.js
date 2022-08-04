// element that will be wrapped
var el = document.querySelectorAll('table.docutils');

el.forEach((item)=>{
    // create wrapper container
    var wrapper = document.createElement('div');
    wrapper.setAttribute("style", "overflow-x:scroll;");
    // insert wrapper before el in the DOM tree
    item.parentNode.insertBefore(wrapper, item);
    // move el into wrapper
    wrapper.appendChild(item);
})