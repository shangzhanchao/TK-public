import { createApp, defineAsyncComponent } from 'vue';

const App = {
  template: `
    <div>
      <HeaderSection />
      <BannerSection />
      <ProductTabs />
      <BrandSection />
      <TechShowcase />
      <CustomerReviews />
      <FooterSection />
    </div>
  `
};

const HeaderSection = defineAsyncComponent(() => import('./components/Header.js'));
const BannerSection = defineAsyncComponent(() => import('./components/Banner.js'));
const ProductTabs = defineAsyncComponent(() => import('./components/ProductTabs.js'));
const BrandSection = defineAsyncComponent(() => import('./components/BrandSection.js'));
const TechShowcase = defineAsyncComponent(() => import('./components/TechShowcase.js'));
const CustomerReviews = defineAsyncComponent(() => import('./components/CustomerReviews.js'));
const FooterSection = defineAsyncComponent(() => import('./components/FooterSection.js'));

createApp(App)
  .component('HeaderSection', HeaderSection)
  .component('BannerSection', BannerSection)
  .component('ProductTabs', ProductTabs)
  .component('BrandSection', BrandSection)
  .component('TechShowcase', TechShowcase)
  .component('CustomerReviews', CustomerReviews)
  .component('FooterSection', FooterSection)
  .mount('#app');
