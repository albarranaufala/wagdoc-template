document.querySelectorAll(".doc-richtext p code").forEach(function (el) {
  // check if <code> has no sibling and has no text in the next or prev
  if (el.previousSibling && el.nextSibling) {
    el.classList.add("inline-code");
    return;
  }

  // turn <br> to \n
  el.innerHTML = el.innerHTML.replace(/<br>/g, "\n");

  // make parent from <p> to <pre>
  const parent = el.parentNode;
  const pre = document.createElement("pre");
  parent.parentNode.replaceChild(pre, parent);
  pre.appendChild(el);
});

hljs.highlightAll();
