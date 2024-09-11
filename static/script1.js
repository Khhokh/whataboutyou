// const btnScrollTo = document.querySelector(".btn-new");
// const section1 = document.querySelector(".cen");
// btnScrollTo.addEventListener('click',function(e){
//     // const s1coords = section1.getBoundingClientRect();
//     // console.log(s1coords);
//     // console.log(e.target.getBoundingClientRect());
//     // console.log('currentScroll (X/Y',window.pageXOffset,window.pageYOffset);
//     // console.log('height/width viewport',document.documentElement.clientHeight,
//     //                                     document.documentElement.clientWidth
//     // );
//     // //scroll
//     // window.scrollTo({
//     //   left:  s1coords.left + window.pageXOffset,
//     //   top:  s1coords.top + window.pageYOffset,
//     //   behavior:'smooth',
//     // });
//     section1.scrollIntoView({behavior:"smooth"});
// });




const allSections = document.querySelectorAll('.section');
const revealSection = function (entries, observer) {
  const [entry] = entries;
  console.log(entry);

  if (!entry.isIntersecting) return;

  entry.target.classList.remove('section--hidden');
  observer.unobserve(entry.target);
};

const sectionObserver = new IntersectionObserver(revealSection, {
  root: null,
  threshold: 0.15,
});

const nav = document.querySelector('.nav');
const btnScrollTo = document.querySelector(".btn-new");
const section1 = document.querySelector(".cen");
btnScrollTo.addEventListener('click',function(e){
    section1.scrollIntoView({behavior:"smooth"});
});

document.querySelector('.nav__links').addEventListener('click', function (e) {
  e.preventDefault();
  if (e.target.classList.contains('nav__link')) {
    const id = e.target.getAttribute('href');
    document.querySelector(id).scrollIntoView({ behavior: 'smooth' });
  }
});



const header = document.querySelector('.header');
const navHeight = nav.getBoundingClientRect().height;
console.log(navHeight)

const stickyNav = function (entries) {
    const [entry] = entries;
    // console.log(entry);
    if (!entry.isIntersecting) nav.classList.add('sticky');
    else nav.classList.remove('sticky');
  };

  const headerObserver = new IntersectionObserver(stickyNav, {
    root: null,
    threshold: 0,
    rootMargin: `-${navHeight}px`,
  });

  headerObserver.observe(header);




allSections.forEach(function (section) {
  sectionObserver.observe(section);
  section.classList.add('section--hidden');
});
