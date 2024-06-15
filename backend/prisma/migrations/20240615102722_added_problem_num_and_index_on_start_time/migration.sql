/*
  Warnings:

  - Added the required column `problem_num_in_contest` to the `problem` table without a default value. This is not possible if the table is not empty.

*/
-- AlterTable
ALTER TABLE "problem" ADD COLUMN     "problem_num_in_contest" INTEGER NOT NULL;

-- CreateIndex
CREATE INDEX "contest_start_time_idx" ON "contest"("start_time");
