-- CreateTable
CREATE TABLE "contest" (
    "title_slug" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "start_time" INTEGER NOT NULL,
    "done" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "contest_pkey" PRIMARY KEY ("title_slug")
);

-- CreateTable
CREATE TABLE "problem" (
    "title_slug" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "credit" INTEGER NOT NULL,
    "contest_title_slug" TEXT NOT NULL,

    CONSTRAINT "problem_pkey" PRIMARY KEY ("title_slug")
);

-- AddForeignKey
ALTER TABLE "problem" ADD CONSTRAINT "problem_contest_title_slug_fkey" FOREIGN KEY ("contest_title_slug") REFERENCES "contest"("title_slug") ON DELETE RESTRICT ON UPDATE CASCADE;
