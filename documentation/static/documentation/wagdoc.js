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

// Sidebar expand and collapse
const burger = document.getElementById("burger");
const sidebar = document.getElementById("sidebar");

burger.addEventListener("click", () => {
  sidebar.classList.toggle("-translate-x-full");
});

// Search functionality
const searchDom = document.getElementById("search");
const searchResultDom = document.getElementById("search-result");

const fetchResult = async (query) => {
  const response = await fetch(`/search-docs/?query=${query}`);
  const data = await response.json();

  setSearchResult(data.pages);
};

let isShowingResult = false;
const setIsShowingResult = (value) => {
  isShowingResult = value;

  if (isShowingResult) {
    searchResultDom.classList.remove("hidden");
  } else {
    searchResultDom.classList.add("hidden");
  }
};

let query = "";
const setQuery = (value) => {
  query = value;

  fetchResult(query);
};

let searchResult = [];
const setSearchResult = (value) => {
  searchResult = value;

  if (searchResult.length > 0) {
    setIsShowingResult(true);
    searchResultDom.innerHTML = searchResult
      .map((page) => {
        return `
                <a href="${page.url}" class="block px-4 py-2 text-sm rounded hover:bg-gray-100">
                    <span class="font-medium">${page.title}</span><br>
                    <span class="text-xs">${page.body}</span>
                </a>
            `;
      })
      .join("");
  } else {
    setIsShowingResult(false);
  }
};

searchDom.addEventListener("input", (e) => {
  setQuery(e.target.value);
});

document.addEventListener("click", (e) => {
  if (!searchDom.contains(e.target) && !searchResultDom.contains(e.target)) {
    setIsShowingResult(false);
  } else {
    fetchResult(query);
  }
});
