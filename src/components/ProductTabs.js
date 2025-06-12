import { defineComponent, ref } from 'vue';
import ProductCard from './ProductCard.js';

export default defineComponent({
  name: 'ProductTabs',
  components: { ProductCard },
  setup() {
    const tabs = [
      { name: '机器人本体', key: 'body' },
      { name: '零部件', key: 'parts' },
      { name: '租赁服务', key: 'rent' }
    ];
    const active = ref('body');
    const products = ref({
      body: [
        { id: 1, name: '人形机器人', desc: '多功能人形机器人', price: '5999', img: 'https://via.placeholder.com/200x160?text=Robot' },
        { id: 2, name: '协作机械臂', desc: '适用于工业制造', price: '8999', img: 'https://via.placeholder.com/200x160?text=Arm' }
      ],
      parts: [
        { id: 3, name: '伺服电机', desc: '高精度电机', price: '399', img: 'https://via.placeholder.com/200x160?text=Motor' }
      ],
      rent: [
        { id: 4, name: '机器人租赁', desc: '短期租赁方案', price: null, img: 'https://via.placeholder.com/200x160?text=Rent' }
      ]
    });
    return { tabs, active, products };
  },
  template: `
    <section class="my-8 px-4">
      <div class="flex space-x-4 border-b">
        <button v-for="tab in tabs" :key="tab.key" @click="active = tab.key" :class="['py-2', active === tab.key ? 'border-b-2 border-blue-600 text-blue-600' : 'text-gray-500']">{{ tab.name }}</button>
      </div>
      <div class="grid grid-cols-2 md:grid-cols-3 lg:grid-cols-4 gap-4 mt-4">
        <ProductCard v-for="item in products[active]" :key="item.id" :product="item" />
      </div>
    </section>
  `
});
