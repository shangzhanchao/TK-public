import { defineComponent } from 'vue';

export default defineComponent({
  name: 'CustomerReviews',
  setup() {
    const reviews = [
      { id: 1, company: '某大型制造企业', comment: '机器人稳定可靠，极大提升了生产效率。' },
      { id: 2, company: '知名教育机构', comment: '教育机器人深受学生喜爱，编程教学效果显著。' }
    ];
    return { reviews };
  },
  template: `
    <section class="bg-gray-50 py-8 px-4">
      <h2 class="text-2xl font-bold mb-4 text-center">客户评价</h2>
      <div class="max-w-3xl mx-auto space-y-4">
        <div v-for="item in reviews" :key="item.id" class="border rounded-lg p-4">
          <h3 class="font-semibold">{{ item.company }}</h3>
          <p class="text-gray-600 text-sm mt-1">{{ item.comment }}</p>
        </div>
      </div>
    </section>
  `
});
