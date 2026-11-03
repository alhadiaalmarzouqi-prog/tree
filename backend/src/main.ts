import { INestApplication } from '@nestjs/common';
import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

/**
 * Creates the application with the shared global configuration.
 * Used by both `bootstrap()` (the HTTP server) and the e2e test, so the
 * test exercises the same wiring that ships.
 */
export async function createApp(): Promise<INestApplication> {
  const app = await NestFactory.create(AppModule);
  app.setGlobalPrefix('api/v1');
  return app;
}

async function bootstrap(): Promise<void> {
  const app = await createApp();
  const port = Number(process.env.PORT ?? 3000);
  await app.listen(port);
}

if (typeof require !== 'undefined' && require.main === module) {
  void bootstrap();
}
