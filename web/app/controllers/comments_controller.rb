class CommentsController < ApplicationController
  def create
    @article = Blogg.find(params[:blogg_id])
    @comment = @article.comments.create(comment_params)
    redirect_to blogg_path(@article)
  end

  def destroy
    @article = Blogg.find(params[:blogg_id])
    @comment = @article.comments.find(params[:id])
    @comment.destroy
    redirect_to blogg_path(@article)
  end

  private
  def comment_params
    params.require(:comment).permit(:commenter, :body)
  end
end
