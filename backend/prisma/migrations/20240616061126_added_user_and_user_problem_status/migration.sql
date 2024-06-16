-- CreateEnum
CREATE TYPE "problem_status" AS ENUM ('SOLVED', 'REVISIT', 'COMPLETED');

-- CreateTable
CREATE TABLE "user" (
    "user_id" TEXT NOT NULL,
    "email" TEXT NOT NULL,
    "username" TEXT NOT NULL,

    CONSTRAINT "user_pkey" PRIMARY KEY ("user_id")
);

-- CreateTable
CREATE TABLE "user_problem_status" (
    "id" TEXT NOT NULL,
    "user_id" TEXT NOT NULL,
    "problem_title_slug" TEXT NOT NULL,
    "status" "problem_status" NOT NULL,

    CONSTRAINT "user_problem_status_pkey" PRIMARY KEY ("id")
);

-- CreateIndex
CREATE UNIQUE INDEX "user_email_key" ON "user"("email");

-- CreateIndex
CREATE INDEX "user_problem_status_user_id_problem_title_slug_idx" ON "user_problem_status"("user_id", "problem_title_slug");

-- CreateIndex
CREATE UNIQUE INDEX "user_problem_status_user_id_problem_title_slug_key" ON "user_problem_status"("user_id", "problem_title_slug");

-- AddForeignKey
ALTER TABLE "user_problem_status" ADD CONSTRAINT "user_problem_status_user_id_fkey" FOREIGN KEY ("user_id") REFERENCES "user"("user_id") ON DELETE RESTRICT ON UPDATE CASCADE;

-- AddForeignKey
ALTER TABLE "user_problem_status" ADD CONSTRAINT "user_problem_status_problem_title_slug_fkey" FOREIGN KEY ("problem_title_slug") REFERENCES "problem"("title_slug") ON DELETE RESTRICT ON UPDATE CASCADE;
