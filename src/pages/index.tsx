import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';

import styles from './index.module.css';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg margin-right--md"
            to="/docs/es-k70/intro">
            ES-K70 — เริ่มอ่าน
          </Link>
          <Link
            className="button button--outline button--secondary button--lg"
            to="/catalog">
            ดูคู่มือทั้งหมด
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home(): ReactNode {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={siteConfig.title}
      description="คู่มือ EPIC ทุกรุ่น — อ่านออนไลน์ ภาษาไทย/อังกฤษ">
      <HomepageHeader />
      <main className="container margin-vert--xl">
        <section className="row">
          <div className="col col--12">
            <Heading as="h2">เกี่ยวกับเว็บไซต์นี้</Heading>
            <p>
              เว็บไซต์นี้รวบรวมคู่มือการใช้งานผลิตภัณฑ์ <strong>EPIC Door Lock</strong> ทุกรุ่น
              ในรูปแบบอ่านง่าย รองรับทั้งภาษาไทยและอังกฤษ เปลี่ยนภาษาได้จากเมนูด้านบนขวา
            </p>
            <p>
              แหล่งที่มา: <a href="https://www.epic.co.kr/home/manual/" target="_blank" rel="noopener noreferrer">epic.co.kr/home/manual</a>
            </p>
          </div>
        </section>

        <section className="row margin-top--lg">
          <div className="col col--4">
            <div className="manual-card">
              <h3 className="manual-card__title">ES-K70 — ครบทุกฟีเจอร์</h3>
              <p>คู่มือฉบับเต็ม: ภาพรวม, ข้อมูลจำเพาะ, ส่วนประกอบ, การลงทะเบียน PIN, การลงทะเบียน/ลบบัตร RFID</p>
              <div className="manual-card__actions">
                <Link className="button button--primary button--sm" to="/docs/es-k70/intro">
                  อ่านเลย →
                </Link>
              </div>
            </div>
          </div>
          <div className="col col--4">
            <div className="manual-card">
              <h3 className="manual-card__title">คู่มือทั้งหมด</h3>
              <p>สารบัญคู่มือทั้ง 22 เล่ม (16 รุ่น + 4 คู่มือ + 1 App + 1 Consolidated)</p>
              <div className="manual-card__actions">
                <Link className="button button--primary button--sm" to="/catalog">
                  เปิดสารบัญ →
                </Link>
              </div>
            </div>
          </div>
          <div className="col col--4">
            <div className="manual-card">
              <h3 className="manual-card__title">EPIC ประเทศไทย</h3>
              <p>ติดต่อฝ่ายขายและบริการหลังการขายผ่านช่องทางต่างๆ</p>
              <div className="manual-card__actions">
                <a className="button button--primary button--sm" href="https://epicdoorlock.com" target="_blank" rel="noopener noreferrer">
                  epicdoorlock.com ↗
                </a>
              </div>
            </div>
          </div>
        </section>
      </main>
    </Layout>
  );
}
