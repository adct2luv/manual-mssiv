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
};

const PRODUCT_MANUALS: Manual[] = [
  {title: 'EF-8000L', slug: 'ef-8000l', category: 'product', size: '5.5 MB'},
  {title: 'EF-P8800K', slug: 'ef-p8800k', category: 'product', size: '3.7 MB', image: '/img/brochures/ef-p8800k.png'},
  {title: 'ES-303G', slug: 'es-303g', category: 'product', size: '3.8 MB', image: '/img/brochures/es-303g.png'},
  {title: 'ES-809L', slug: 'es-809l', category: 'product', size: '6.5 MB'},
  {title: 'ES-B10', slug: 'es-b10', category: 'product', size: '14 MB', image: '/img/brochures/es-b10.png'},
  {title: 'ES-K70', slug: 'es-k70', category: 'product', size: '8.2 MB'},
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
  {title: 'คู่มือประกอบ Key Tail', slug: 'assembly-guide-for-key-tail', category: 'guide', size: '0.4 MB'},
  {title: 'IR Sensor สำหรับ Face ID', slug: 'ir-sensor-usage-guide-for-face-id', category: 'guide', size: '0.5 MB'},
  {title: 'การจัดการสายของตัวล็อกด้านนอก', slug: 'outer-body-cable-management-guide', category: 'guide', size: '0.1 MB'},
  {title: 'ตารางความเข้ากันได้ของ Remote Control', slug: 'remote-control-module-compatibility-guide', category: 'guide', size: '0.1 MB'},
];

const APP_AND_CONSOLIDATED: Manual[] = [
  {title: 'Consolidated Manual (Rev.09)', slug: 'consolidated-manual-rev-09', category: 'consolidated', size: '5.7 MB'},
  {title: 'EPIC Things APP', slug: 'epic-things-app-user-manual', category: 'app', size: '9.4 MB'},
];

function ManualCard({m, localePrefix = ''}: {m: Manual; localePrefix?: string}) {
  const introUrl = `${localePrefix}/${m.slug}/intro`;
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
        <div className="manual-card__actions">
          <Link className="button button--primary button--sm button--block" to={introUrl}>
            📖 อ่านคู่มือ
          </Link>
        </div>
      </div>
    </div>
  );
}

function ManualGrid({manuals, localePrefix = ''}: {manuals: Manual[]; localePrefix?: string}) {
  return (
    <div className="row">
      {manuals.map((m) => (
        <ManualCard key={m.slug} m={m} localePrefix={localePrefix} />
      ))}
    </div>
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
          คู่มือทั้งหมด <strong>{PRODUCT_MANUALS.length + REFERENCE_GUIDES.length + APP_AND_CONSOLIDATED.length} เล่ม</strong> จาก <a href="https://www.epic.co.kr/home/manual/" target="_blank" rel="noopener noreferrer">epic.co.kr/home/manual/</a>
          {' '}— ปรับปรุงล่าสุด 2026-06-17
        </p>

        <section className="margin-top--lg">
          <Heading as="h2">คู่มือรายรุ่น ({PRODUCT_MANUALS.length})</Heading>
          <p>คู่มือการใช้งานสำหรับกุญแจดิจิทัล EPIC แต่ละรุ่น — คลิกที่การ์ดเพื่ออ่าน</p>
          <ManualGrid manuals={PRODUCT_MANUALS} />
        </section>

        <section className="margin-top--lg">
          <Heading as="h2">คู่มือติดตั้งและอ้างอิง ({REFERENCE_GUIDES.length})</Heading>
          <p>คู่มือข้ามรุ่นสำหรับการติดตั้งและความเข้ากันได้</p>
          <ManualGrid manuals={REFERENCE_GUIDES} />
        </section>

        <section className="margin-top--lg">
          <Heading as="h2">App และ Consolidated ({APP_AND_CONSOLIDATED.length})</Heading>
          <p>คู่มือแอปและคู่มือรวม</p>
          <ManualGrid manuals={APP_AND_CONSOLIDATED} />
        </section>

        <p className="margin-top--xl">
          <small>
            ทุกคู่มือเป็นแบบสองภาษา (ไทย/อังกฤษ) คลิกปุ่มเปลี่ยนภาษาที่มุมขวาบน หรือเพิ่ม <code>/en/</code> ต่อท้าย URL
          </small>
        </p>
      </main>
    </Layout>
  );
}
