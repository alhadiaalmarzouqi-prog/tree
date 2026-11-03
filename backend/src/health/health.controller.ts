import { Controller, Get } from '@nestjs/common';

export interface HealthStatus {
  status: 'ok';
  service: 'sovereign-lineage-backend';
}

@Controller('health')
export class HealthController {
  @Get()
  check(): HealthStatus {
    return { status: 'ok', service: 'sovereign-lineage-backend' };
  }
}
