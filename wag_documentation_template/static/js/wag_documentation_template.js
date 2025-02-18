document
  .querySelectorAll(".doc-richtext p code:first-child:last-child")
  .forEach(function (el) {
    // turn <br> to \n
    el.innerHTML = el.innerHTML.replace(/<br>/g, "\n");

    // make parent from <p> to <pre>
    const parent = el.parentNode;
    const pre = document.createElement("pre");
    parent.parentNode.replaceChild(pre, parent);
    pre.appendChild(el);
  });

hljs.highlightAll();
