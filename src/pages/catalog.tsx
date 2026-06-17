import type {ReactNode} from 'react';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import Link from '@docusaurus/Link';

type Manual = {
  title: string;
  slug: string;
  category: 'product' | 'guide' | 'app' | 'consolidated';
  size: string;
  image?: string;
  onlinePath?: string;
};

const PRODUCT_MANUALS: Manual[] = [
  {title: 'EF-8000L', slug: 'ef-8000l', category: 'product', size: '5.5 MB'},
  {title: 'EF-P8800K', slug: 'ef-p8800k', category: 'product', size: '3.7 MB', image: '/img/brochures/ef-p8800k.png'},
  {title: 'ES-303G', slug: 'es-303g', category: 'product', size: '3.8 MB', image: '/img/brochures/es-303g.png'},
  {title: 'ES-809L', slug: 'es-809l', category: 'product', size: '6.5 MB'},
  {title: 'ES-B10', slug: 'es-b10', category: 'product', size: '14 MB', image: '/img/brochures/es-b10.png'},
  {title: 'ES-K70', slug: 'es-k70', category: 'product', size: '8.2 MB', onlinePath: '/es-k70/intro'},
  {title: 'ES-L200 Series', slug: 'es-l200', category: 'product', size: '252 KB', image: '/img/brochures/es-l200.png'},
  {title: 'ES-M50', slug: 'es-m50', category: 'product', size: '3.1 MB', image: '/img/brochures/es-m50.png'},
  {title: 'ES-P9100FK', slug: 'es-p9100fk', category: 'product', size: '10 MB'},
  {title: 'ES-T153', slug: 'es-t153', category: 'product', size: '20 MB'},
  {title: 'N-TOUCH', slug: 'n-touch', category: 'product', size: '5.9 MB', image: '/img/brochures/n-touch.png'},
  {title: 'OS300H', slug: 'os300h', category: 'product', size: '0.8 MB', image: '/img/brochures/os300h.png'},
  {title: 'POPscan', slug: 'popscan', category: 'product', size: '12 MB', image: '/img/brochures/popscan.png'},
  {title: 'TOUCH', slug: 'touch', category: 'product', size: '13 MB', image: '/img/brochures/touch.png'},
  {title: 'TRIPLEX 2way', slug: 'triplex-2way', category: 'product', size: '14 MB'},
  {title: 'TRIPLEX 3way', slug: 'triplex-3way', category: 'product', size: '17 MB'},
];

const REFERENCE_GUIDES: Manual[] = [
  {title: 'คู่มือประกอบ Key Tail', slug: 'key-tail-assembly', category: 'guide', size: '0.4 MB'},
  {title: 'Consolidated Manual (Rev.09)', slug: 'consolidated-manual', category: 'consolidated', size: '5.7 MB'},
  {title: 'คู่มือใช้งาน IR Sensor สำหรับ Face ID', slug: 'ir-sensor-face-id', category: 'guide', size: '0.5 MB'},
  {title: 'คู่มือจัดการสายของตัวล็อกด้านนอก', slug: 'outer-body-cable', category: 'guide', size: '0.1 MB'},
  {title: 'ตารางความเข้ากันได้ของ Remote Control', slug: 'remote-control-compat', category: 'guide', size: '0.1 MB'},
];

const APP_MANUALS: Manual[] = [
  {title: 'EPIC Things APP', slug: 'epic-things-app', category: 'app', size: '9.4 MB'},
];

function ManualCard({m}: {m: Manual}) {
  return (
    <div className="col col--4 margin-bottom--lg">
      <div className="manual-card">
        {m.image && (
          <img
            src={m.image}
            alt={m.title}
            style={{width: '100%', height: '180px', objectFit: 'contain', marginBottom: '0.75rem', background: '#fafafa'}}
          />
        )}
        <div>
          <h3 className="manual-card__title">{m.title}</h3>
          <p className="manual-card__meta">{m.size} · {m.category}</p>
        </div>
      </div>
    </div>
  );
}

function ManualGrid({manuals, title, description}: {manuals: Manual[]; title: string; description?: string}) {
  return (
    <section className="margin-top--lg">
      <Heading as="h2">{title} ({manuals.length})</Heading>
      {description && <p>{description}</p>}
      <div className="row">
        {manuals.map((m) => (
          <ManualCard key={m.slug} m={m} />
        ))}
      </div>
    </section>
  );
}

export default function Catalog(): ReactNode {
  return (
    <Layout
      title="สารบัญคู่มือทั้งหมด"
      description="สารบัญคู่มือ EPIC ทั้ง 22 เล่ม — สินค้า คู่มืออ้างอิง และแอป"
    >
      <main className="container margin-vert--lg">
        <Heading as="h1">สารบัญคู่มือทั้งหมด</Heading>
        <p>
          คู่มือทั้งหมด <strong>{PRODUCT_MANUALS.length + REFERENCE_GUIDES.length + APP_MANUALS.length} เล่ม</strong> จาก <a href="https://www.epic.co.kr/home/manual/" target="_blank" rel="noopener noreferrer">epic.co.kr/home/manual/</a>
          {' '}— ปรับปรุงล่าสุด 2026-06-16
        </p>

        <ManualGrid
          manuals={PRODUCT_MANUALS}
          title="คู่มือรายรุ่น"
          description="คู่มือการใช้งานสำหรับกุญแจดิจิทัล EPIC แต่ละรุ่น"
        />
        <ManualGrid
          manuals={REFERENCE_GUIDES}
          title="คู่มือติดตั้งและอ้างอิง"
          description="คู่มือข้ามรุ่นสำหรับการติดตั้งและความเข้ากันได้"
        />
        <ManualGrid
          manuals={APP_MANUALS}
          title="แอปและซอฟต์แวร์"
        />

        <p className="margin-top--xl">
          <small>
            หมายเหตุ: ขณะนี้มีเพียง <strong>ES-K70</strong> ที่มีคู่มือออนไลน์ฉบับเต็ม รุ่นอื่น ๆ กำลังจะตามมา — ดู <Link to="/es-k70/intro">ตัวอย่างคู่มือ ES-K70</Link>
          </small>
        </p>
      </main>
    </Layout>
  );
}
