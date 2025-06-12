import { defineComponent } from 'vue';

export default defineComponent({
  name: 'TechShowcase',
  setup() {
    const scenes = [
      { id: 1, title: '教育场景', img: 'https://via.placeholder.com/300x200?text=Edu', desc: '助力教育机器人解决方案' },
      { id: 2, title: '智能制造', img: 'https://via.placeholder.com/300x200?text=Factory', desc: '协作机器人提升产能' },
      { id: 3, title: '家庭服务', img: 'https://via.placeholder.com/300x200?text=Home', desc: '贴心家庭机器人' },
      { id: 4, title: '医疗辅助', img: 'https://via.placeholder.com/300x200?text=Medical', desc: '手术辅助与康复机器人' }
    ];
    return { scenes };
  },
  template: `
    <section class="py-8 px-4">
      <h2 class="text-2xl font-bold mb-4 text-center">技术与应用场景</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
        <div v-for="item in scenes" :key="item.id" class="border rounded-lg p-4 flex flex-col items-center text-center">
          <img :src="item.img" class="w-full h-40 object-cover" alt="scene" />
          <h3 class="mt-2 font-semibold">{{ item.title }}</h3>
          <p class="text-sm text-gray-500">{{ item.desc }}</p>
        </div>
      </div>
    </section>
  `
});
