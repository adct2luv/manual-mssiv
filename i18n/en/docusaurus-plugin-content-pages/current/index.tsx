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
            to="/es-k70/intro">
            ES-K70 — Start reading
          </Link>
          <Link
            className="button button--outline button--secondary button--lg"
            to="/catalog">
            Browse all manuals
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
      description="EPIC product manuals online — Thai & English">
      <HomepageHeader />
      <main className="container margin-vert--xl">
        <section className="row">
          <div className="col col--12">
            <Heading as="h2">About this site</Heading>
            <p>
              This site collects user manuals for every <strong>EPIC Door Lock</strong> model
              in an easy-to-read format. Available in both Thai and English — switch languages
              using the menu in the top-right corner.
            </p>
            <p>
              Source: <a href="https://www.epic.co.kr/home/manual/" target="_blank" rel="noopener noreferrer">epic.co.kr/home/manual</a>
            </p>
          </div>
        </section>

        <section className="row margin-top--lg">
          <div className="col col--4">
            <div className="manual-card">
              <h3 className="manual-card__title">ES-K70 — Full manual</h3>
              <p>Complete user guide: overview, specs, components, PIN registration, RFID registration & deletion</p>
              <div className="manual-card__actions">
                <Link className="button button--primary button--sm" to="/es-k70/intro">
                  Read now →
                </Link>
              </div>
            </div>
          </div>
          <div className="col col--4">
            <div className="manual-card">
              <h3 className="manual-card__title">All manuals</h3>
              <p>Catalogue of all 22 manuals (16 product manuals + 4 guides + 1 app + 1 consolidated)</p>
              <div className="manual-card__actions">
                <Link className="button button--primary button--sm" to="/catalog">
                  Open catalogue →
                </Link>
              </div>
            </div>
          </div>
          <div className="col col--4">
            <div className="manual-card">
              <h3 className="manual-card__title">EPIC Thailand</h3>
              <p>Sales and after-sales support contacts</p>
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
