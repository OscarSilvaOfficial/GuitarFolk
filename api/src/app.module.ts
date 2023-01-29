import { Module } from '@nestjs/common';
import { AppController } from './controllers/app.controller';
import { PROVIDERS } from './providers';

@Module({
  controllers: [AppController],
  providers: [PROVIDERS.MONGO_SERVICE],
})
export class AppModule {}
