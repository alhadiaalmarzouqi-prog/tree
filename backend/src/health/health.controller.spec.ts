import { HealthController } from './health.controller';

describe('HealthController', () => {
  let controller: HealthController;

  beforeEach(() => {
    controller = new HealthController();
  });

  it('reports ok status for the backend service', () => {
    expect(controller.check()).toEqual({
      status: 'ok',
      service: 'sovereign-lineage-backend',
    });
  });
});
