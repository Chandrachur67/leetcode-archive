-- CreateTable
CREATE TABLE "Contest" (
    "titleSlug" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "startTime" INTEGER NOT NULL,
    "done" BOOLEAN NOT NULL DEFAULT false,

    CONSTRAINT "Contest_pkey" PRIMARY KEY ("titleSlug")
);

-- CreateTable
CREATE TABLE "Problem" (
    "titleSlug" TEXT NOT NULL,
    "title" TEXT NOT NULL,
    "credit" INTEGER NOT NULL,
    "contestTitleSlug" TEXT NOT NULL,

    CONSTRAINT "Problem_pkey" PRIMARY KEY ("titleSlug")
);

-- AddForeignKey
ALTER TABLE "Problem" ADD CONSTRAINT "Problem_contestTitleSlug_fkey" FOREIGN KEY ("contestTitleSlug") REFERENCES "Contest"("titleSlug") ON DELETE RESTRICT ON UPDATE CASCADE;
