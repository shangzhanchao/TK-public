import { defineComponent } from 'vue';

export default defineComponent({
  name: 'BrandSection',
  template: `
    <section class="bg-gray-100 py-8 px-4 text-center">
      <h2 class="text-2xl font-bold mb-2">品牌故事</h2>
      <p class="max-w-3xl mx-auto text-gray-600">我们致力于机器人技术的研发与应用，拥有丰富的行业经验与优秀的合作伙伴，为客户提供高质量的产品与服务。</p>
    </section>
  `
});
